from random import choice, randint, shuffle

class Basic():
    profile_name: str
    is_add = False
    is_sub = False
    is_mul = False
    is_div = False
    is_mul_range = False
    is_mul_max_result = False
    add_range = [0, 100]
    sub_range = [0, 100]
    mul_range = [0, 10]
    mul_max_result = 100
    div_max_result = 100
    num_of_ops = 1
    with_negative_result = False
    more_than_one_mul_or_div = False

    def __init__(self, Data):
        operations = []

        self.is_add = Data.is_add
        self.is_sub = Data.is_sub
        self.is_mul = Data.is_mul
        self.is_div = Data.is_div
        self.is_mul_range = Data.is_mul_range
        self.is_mul_max_result = Data.is_mul_max_result
        self.mul_range = Data.mul_range
        self.mul_max_result = Data.mul_max_result
        self.div_max_result = Data.div_max_result
        self.num_of_ops = Data.num_of_ops
        self.more_than_one_mul_or_div = Data.more_than_one_mul_or_div

        operations.append("+") if self.is_add else False
        operations.append("-") if self.is_sub else False
        operations.append("*") if self.is_mul else False
        operations.append("/") if self.is_div else False

        operations = self.get_op_flow(operations)
        task = self.create_task(operations)

        print(f'{self.task_list_to_str(task)} = {int(self.task_list_eval(task))}')

    def addition(self, min, max):
        if min >= max: return False
        x = randint(min, max)
        y = randint(min, 100 - x)
        return [x, '+', y]

    def subtract(self, min, max):
        if min >= max: return False
        x = randint(min, max)
        y = randint(0, x)
        return [x, '-',y]

    def multiply(self,
                 is_mul_range = False,
                 is_mul_result = False,
                 min_range = 0,
                 max_range = 10,
                 max_result = 100):
        if not is_mul_range and not is_mul_result: is_mul_range = True
        if is_mul_range:
            x = randint(min_range, max_range)
            y = randint(min_range, max_range)
            return [x, '*',y]
        if is_mul_result:
            x = randint(1, int(max_result / 2.5))
            y = choice(range(1,int(max_result / x)))
            return [x, '*', y]

    def divide(self, max):
        x = choice(self.get_composite_numbers(max))
        y = choice(self.get_denominators(x))
        r = int(x / y)
        return [x, '/', y]

    def get_nr_to_add(self,current_sum):
        return randint(0, self.add_range[1] - current_sum)

    def get_nr_to_sub(self, current_sum, before_index):
        if before_index:
            return randint(current_sum, self.sub_range[1])
        else:
            return randint(self.sub_range[0], current_sum)

    def get_denominators(self, num):
        """
        Method requires a number and return a list of all possible denominatiors
        :param num:
        :return list nums:
        """
        nums = []
        for i in range(1, num):
            if num % i == 0:
                nums.append(i)
        return nums

    def get_composite_numbers(self, num):
        """
        Requires a number as input and return all composite numbers (non prime numbers)
        :param num:
        :return list nums:
        """
        nums = []
        for i in range(2, num + 1):
            if not self.is_prime_number(i):
                nums.append(i)
        return nums

    def is_prime_number(self, num):
        """
        Taking a number as parameter, and returns a boolean.
        True - is the number is a prime number (divisible only by itself and the number 1)
        False - if number is less than 2, or is not an prime number
        :param num:
        :return bool:
        """
        if num < 2: return False
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    return False
                    break
        return True

    def get_random_operation_task(self, ops):
        op = choice(ops)
        if op == '+': return self.addition(self.add_range[0], self.add_range[1])
        if op == '-': return self.subtract(self.sub_range[0], self.sub_range[1])
        if op == '*': return self.multiply(is_mul_range=self.is_mul_range,
                                           is_mul_result=self.is_mul_max_result,
                                           min_range=self.mul_range[0],
                                           max_range=self.mul_range[1],
                                           max_result=self.mul_max_result)
        if op == '/': return self.divide(self.div_max_result)

    def get_op_flow(self, ops):
        op_flow = []
        ops_added = 0
        while ops_added < self.num_of_ops:
            op = choice(ops)
            if not self.more_than_one_mul_or_div and (op == "*" or op == "/"):
                while "*" in ops: ops.remove("*")
                while "/" in ops: ops.remove("/")
            op_flow.append(op)
            ops_added += 1
        shuffle(op_flow)
        return op_flow

    def create_task(self, ops):
        created_ops = 0
        current = []
        full_task = []
        current_result = 0
        index = False

        if '*' in ops:
            index = ops.index("*")
            current = self.get_random_operation_task(ops.pop(ops.index("*")))
        elif '/' in ops:
            index = ops.index("/")
            current = self.get_random_operation_task(ops.pop(ops.index("/")))
        else:
            current = self.get_random_operation_task(ops.pop(0))
        created_ops += 1
        full_task += current
        if created_ops < self.num_of_ops:
            if index:
                for i in range(index - 1, -1, -1):
                    if ops[i] == '+':
                        num = self.get_nr_to_add(self.task_list_eval(full_task))
                        full_task = [num, '+'] + full_task
                    elif ops[i] == '-':
                        num = self.get_nr_to_sub(self.task_list_eval(full_task), True)
                        full_task = [num, '-'] + full_task

                for i in range(index, self.num_of_ops):
                    if index < self.num_of_ops: break
                    if ops[i] == "+":
                        num = self.get_nr_to_add(self.task_list_eval(full_task))
                        full_task += ['+', num]
                    elif ops[i] == "-":
                        num = self.get_nr_to_sub(self.task_list_eval(full_task), False)
                        full_task += ['-', num]

            else:

                while ops:
                    if ops[0] == '+':
                        num = self.get_nr_to_add(self.task_list_eval(full_task))
                        full_task += [ops.pop(0), num]
                    elif ops[0] == '-':
                        num = self.get_nr_to_sub(self.task_list_eval(full_task), False)
                        full_task += [ops.pop(0), num]
        return full_task

    def task_list_to_str(self, tl):
        return " ".join(map(str, tl))

    def task_list_eval(self, tl):
        return eval(self.task_list_to_str(tl))
