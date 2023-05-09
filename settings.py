class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3  # 一开始玩家拥有的飞船数量

        # 子弹设置
        self.bullet_speed = 1.5  # 子弹的速度比飞船稍低
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 深灰色子弹
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed = 0.6
        self.fleet_drop_speed = 8
        # fleet_direction为1表示向右移，为-1表示向左移。
        self.fleet_direction = 1
