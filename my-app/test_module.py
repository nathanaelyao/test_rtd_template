from typing import List

class Solution:
    """
    A class to generate an array of n unique integers that sum up to 0.
    """
    
    def sumZero(self, n: int) -> List[int]:
        """
        Returns a list of n integers such that their sum is zero.
        
        Parameters
        ----------
        n
            The number of integers to be returned.
        
        Returns
        -------
        List[int] 
            A list of n integers where the sum of the integers is zero.
        """
        
        prefix_sum = 0
        res = []
        # 1, n-1
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        return res

    def sumZero2(self, n: int) -> List[int]:
        """
        Returns a list of n integers such that their sum is zero.
        
        Parameters
        ----------
        n: int
            The number of integers to be returned.
        
        Returns
        -------
            A list of n integers where the sum of the integers is zero.
        """
        
        prefix_sum = 0
        res = []
        # 1, n-1
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        return res
    def sumZero3(self, n: int) -> List[int]:
        """
        Returns a list of n integers such that their sum is zero.
        
        Parameters
        ----------
        n: int
        The number of integers to be returned.
        
        Returns
        -------
        A list of n integers where the sum of the integers is zero.
        """
        
        prefix_sum = 0
        res = []
        # 1, n-1
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        return res

    def sumZero4(self, n: int) -> List[int]:
        """
        Returns a list of n integers such that their sum is zero.
        
        Parameters
        ----------
        n (int)
            The number of integers to be returned.
        
        Returns
        -------
        List[int]
            A list of n integers where the sum of the integers is zero.
        """
        
        prefix_sum = 0
        res = []
        # 1, n-1
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        return res

    def sumZero5(self, n: int) -> List[int]:
        """
        Returns a list of n integers such that their sum is zero.
        
        Parameters
        ----------
        n : (int)
        The number of integers to be returned.
        
        Returns
        -------
        List[int]
        A list of n integers where the sum of the integers is zero.
        """
        
        prefix_sum = 0
        res = []
        # 1, n-1
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        return res
    
    def sumZero6(self, n: int):
        """
        Returns a list of n integers such that their sum is zero.
        
        Parameters
        ----------
        n
            The number of integers to be returned.
        
        Returns
        -------
        : 
            A list of n integers where the sum of the integers is zero.
        """
        
        prefix_sum = 0
        res = []
        # 1, n-1
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        # sum(from 1 to n-1)
        res.append(-prefix_sum)
        return res

    def add_numbers(self, a, b):
        """
        Returns the sum of two numbers.

        Parameters
        ----------
        a : int
            First number
        b : float
            Second number

        Returns
        -------
        sum : int
            The sum of the inputs.

        Attributes
        ----------
        Some attribute : str
            This is unnecessary and should not be included.
        """
        return a + b

    def add_numbers2(self, a, b):
        """Performs addition.
        
        Parameters
        ----------
        a : int
            The first number.
        b : int
            The second number.
        Returns
        -------
        int : sum of a and b"""
        return a + b

    def add_numbers3(self, a, b):
        """
        Adds two numbers.
        
        Parameters
        ----------
        a : int
            First number
        b : int
            Second number
        
        Returns
        -------
        result : int
            Sum of a and b.
        Example:
            >>> example_func(3, 5)
            8
        """
        return a + b
    def add_numbers4(self, a, b):
        """
        Adds two numbers.
        Parameters
        ----------
        a : int
        First number.
        b : int
            Second number.
        
        Returns
        -------
        int : Sum of a and b.
        """
        return a + b
    def add_numbers5(self, a, b):
        """
        Adds two numbers.

        Parameters
        ----------
        a : int
            First number.
        b : int
            Second number.

        Returns
        -------
        result
            Sum of a and b.
        """
        return a + b


