"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class FieldContractService(BaseModuleService):
    MODULE = "field_contract"
    ENTITY = "字段映射"
    OPERATION_TERM = "转换"
    LIST_FIELDS = ["契约编号", "源字段", "目标字段", "数据类型", "转换规则", "必填标记", "默认值", "契约版本"]
    REQUIRED_FIELDS = ["契约编号", "源字段", "目标字段"]
    STATUS_ORDER = ["草稿", "待校验", "已生效", "已废弃"]
    ACTION_RULES = {"提交校验": "待校验", "确认生效": "已生效", "标记废弃": "已废弃"}
    NEGATIVE_ACTIONS = []
