from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import threading

from .data import UserGroup

groups = []


class ExpenseTracker(APIView):

    def post(self, request, group_name):

        """
            Add new expense to group.
        """

        data = request.data

        """
            Code block gets the List of all members in expense.
        """

        members = []

        for item in data['items']:
            for member in item['paid_by'][0]:
                members.append(member)

            for member in item['owed_by'][0]:
                members.append(member)

        """
            Code block checks if Group, expense exists. 
            If expense with same name doesn't exists add new expense to group.
            Update the members of the group.
        """
        for group in groups:
            if group.name == group_name:
                for expense in group.expenses:
                    if expense['name'] == data['name']:
                        return Response({"msg": "Expense with name already exists"}, status=status.HTTP_409_CONFLICT)

                group.add_expense(data)
                group.set_members(set(members))
                return Response({"method ": "Expense added successfully"}, status=status.HTTP_200_OK)

        return Response({"method ": "Group does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, group_name):

        """
            Update expense in group.
        """

        data = request.data

        """
            Code block gets the List of all members in expense.
        """

        members = []

        for item in data['items']:
            for member in item['paid_by'][0]:
                members.append(member)

            for member in item['owed_by'][0]:
                members.append(member)

        """
            Code block checks if Group, expense exists.
            If expense with same name exists update expense.
            Update the members of the group.
        """

        for group in groups:
            if group.name == group_name:
                for expense in group.expenses:
                    if expense['name'] == data['name']:
                        expense = data
                        group.set_members(set(members))
                        return Response({"msg": "Expense updated successfully."}, status=status.HTTP_200_OK)

                return Response({"msg": "Expense does not exist."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"method ": "Group does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, group_name, expense_name):

        """
            Delete expense from group.
        """

        data = request.data

        """
            Code block checks if Group, expense exists.
            If expense with same name exists delete expense.
        """

        for group in groups:
            if group.name == group_name:
                for index in range(len(group.expenses)):
                    if group.expenses[index]['name'] == expense_name:
                        del group.expenses[index]
                        return Response({"msg": "Expense deleted successfully."}, status=status.HTTP_200_OK)

                return Response({"msg": "Expense does not exist."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"method ": "Group does not exist"}, status=status.HTTP_404_NOT_FOUND)


class GroupTracker(APIView):

    def get(self, request):
        data = request.POST
        return Response({"msg ": "Get user details"}, status=status.HTTP_200_OK)

    def post(self, request):

        "Add new group."

        data = request.data

        """
            Code block checks if Group with same name exists.
            If group with same name does not exists create new group.
        """

        for group in groups:
            if group.name == data['name']:
                return Response({"msg": "Group already exists."}, status=status.HTTP_409_CONFLICT)

        groups.append(UserGroup(data['name'], data['members']))

        return Response({"msg": "Group created successfully."}, status=status.HTTP_200_OK)
