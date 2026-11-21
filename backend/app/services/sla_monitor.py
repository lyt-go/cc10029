"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SlaMonitorService(BaseModuleService):
    MODULE = "sla_monitor"
    ENTITY = "时效指标"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["指标编号", "源端编号", "约定到达时限", "实际到达时长", "超时批次数", "迟到率", "统计窗口", "指标版本"]
    REQUIRED_FIELDS = ["指标编号", "源端编号", "约定到达时限"]
    STATUS_ORDER = ["草稿", "待统计", "已统计", "已过期"]
    ACTION_RULES = {"启动统计": "待统计", "确认统计": "已统计", "标记过期": "已过期"}
    NEGATIVE_ACTIONS = []
