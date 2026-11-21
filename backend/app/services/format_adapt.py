"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class FormatAdaptService(BaseModuleService):
    MODULE = "format_adapt"
    ENTITY = "适配版本"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["适配编号", "记录格式", "旧版结构", "新版结构", "差异字段", "兼容方式", "切换批次", "适配版本"]
    REQUIRED_FIELDS = ["适配编号", "记录格式", "旧版结构"]
    STATUS_ORDER = ["草稿", "待适配", "已适配", "已退役"]
    ACTION_RULES = {"提交适配": "待适配", "确认适配": "已适配", "标记退役": "已退役"}
    NEGATIVE_ACTIONS = []
