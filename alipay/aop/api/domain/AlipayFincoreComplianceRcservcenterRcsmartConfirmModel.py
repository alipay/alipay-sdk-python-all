#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcsmartCommonAppInfo import RcsmartCommonAppInfo
from alipay.aop.api.domain.TaskRobotAuditFeedbackReq import TaskRobotAuditFeedbackReq


class AlipayFincoreComplianceRcservcenterRcsmartConfirmModel(object):

    def __init__(self):
        self._app_info = None
        self._task_robot_audit_feedback_req = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        if isinstance(value, RcsmartCommonAppInfo):
            self._app_info = value
        else:
            self._app_info = RcsmartCommonAppInfo.from_alipay_dict(value)
    @property
    def task_robot_audit_feedback_req(self):
        return self._task_robot_audit_feedback_req

    @task_robot_audit_feedback_req.setter
    def task_robot_audit_feedback_req(self, value):
        if isinstance(value, TaskRobotAuditFeedbackReq):
            self._task_robot_audit_feedback_req = value
        else:
            self._task_robot_audit_feedback_req = TaskRobotAuditFeedbackReq.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.task_robot_audit_feedback_req:
            if hasattr(self.task_robot_audit_feedback_req, 'to_alipay_dict'):
                params['task_robot_audit_feedback_req'] = self.task_robot_audit_feedback_req.to_alipay_dict()
            else:
                params['task_robot_audit_feedback_req'] = self.task_robot_audit_feedback_req
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcservcenterRcsmartConfirmModel()
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'task_robot_audit_feedback_req' in d:
            o.task_robot_audit_feedback_req = d['task_robot_audit_feedback_req']
        return o


