"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class RejectRecordService(BaseModuleService):
    MODULE = "reject_record"
    ENTITY = "拒收记录"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["拒收编号", "批次编号", "记录主键", "拒收环节", "拒收原因", "回执编号", "退回目标", "处置时间"]
    REQUIRED_FIELDS = ["拒收编号", "批次编号", "记录主键"]
    STATUS_ORDER = ["草稿", "待处置", "已退回", "已丢弃"]
    ACTION_RULES = {"提交处置": "待处置", "确认退回": "已退回", "标记丢弃": "已丢弃"}
    NEGATIVE_ACTIONS = []
