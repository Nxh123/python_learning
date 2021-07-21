from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])  #决定前进方向
        distance = choice([0, 1, 2, 3, 4])  #决定前进距离
        return direction * distance

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        while len(self.x_values) < self.num_points:
            # x_direction = choice([-1, 1])  #决定前进方向
            # x_distance = choice([0, 1, 2, 3, 4])  #决定前进距离
            # x_step = x_direction * x_distance
            # y_direction = choice([-1, 1])
            # y_distance = choice([0, 1, 2, 3, 4])
            # y_step = y_direction * y_distance
            x_step = self.get_step()
            y_step = self.get_step()
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的坐标
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
