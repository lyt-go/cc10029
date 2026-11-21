"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class TargetRegisterService(BaseModuleService):
    MODULE = "target_register"
    ENTITY = "目标端点"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["目标编号", "系统名称", "接收格式", "落地方式", "批量上限", "确认模式", "回执格式", "登记游标"]
    REQUIRED_FIELDS = ["目标编号", "系统名称", "接收格式"]
    STATUS_ORDER = ["草稿", "待校验", "已登记", "已停用"]
    ACTION_RULES = {"提交校验": "待校验", "确认登记": "已登记", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
