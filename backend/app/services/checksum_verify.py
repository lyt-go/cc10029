"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ChecksumVerifyService(BaseModuleService):
    MODULE = "checksum_verify"
    ENTITY = "校验任务"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["校验编号", "批次编号", "源端校验值", "目标校验值", "分片校验", "差异条数", "校验算法", "校验结论"]
    REQUIRED_FIELDS = ["校验编号", "批次编号", "源端校验值"]
    STATUS_ORDER = ["草稿", "待校验", "校验中", "已通过", "未通过"]
    ACTION_RULES = {"启动校验": "校验中", "判定通过": "已通过", "判定未过": "未通过"}
    NEGATIVE_ACTIONS = []
