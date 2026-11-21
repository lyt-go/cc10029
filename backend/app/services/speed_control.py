"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SpeedControlService(BaseModuleService):
    MODULE = "speed_control"
    ENTITY = "限速策略"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["策略编号", "作用范围", "每秒记录数", "每秒字节数", "突发窗口", "排队上限", "整形算法", "策略版本"]
    REQUIRED_FIELDS = ["策略编号", "作用范围", "每秒记录数"]
    STATUS_ORDER = ["草稿", "待生效", "已生效", "已停用"]
    ACTION_RULES = {"提交生效": "待生效", "确认生效": "已生效", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
