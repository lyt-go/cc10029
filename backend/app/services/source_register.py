"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SourceRegisterService(BaseModuleService):
    MODULE = "source_register"
    ENTITY = "源端系统"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["源端编号", "系统名称", "数据域", "记录格式", "编码方式", "日增量级", "抽取方式", "登记游标"]
    REQUIRED_FIELDS = ["源端编号", "系统名称", "数据域"]
    STATUS_ORDER = ["草稿", "待校验", "已登记", "已停用"]
    ACTION_RULES = {"提交校验": "待校验", "确认登记": "已登记", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
