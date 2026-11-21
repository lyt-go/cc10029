"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ResumePointService(BaseModuleService):
    MODULE = "resume_point"
    ENTITY = "续传断点"
    OPERATION_TERM = "水位"
    LIST_FIELDS = ["断点编号", "批次编号", "已完成分片", "未完成分片", "恢复位置", "重试次数", "断点类型", "续传水位"]
    REQUIRED_FIELDS = ["断点编号", "批次编号", "已完成分片"]
    STATUS_ORDER = ["草稿", "待续传", "续传中", "已恢复"]
    ACTION_RULES = {"启动续传": "续传中", "确认恢复": "已恢复", "标记放弃": "已恢复"}
    NEGATIVE_ACTIONS = []
