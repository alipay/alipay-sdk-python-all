#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskJointdecisionTradeSendModel(object):

    def __init__(self):
        self._out_trade_no = None
        self._payee_account = None
        self._payee_account_open_id = None
        self._pid = None
        self._risk_custom_info = None
        self._risk_trade_feedback = None
        self._risk_trade_feedback_time = None
        self._scene = None
        self._smid = None
        self._task_id = None
        self._trade_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payee_account_open_id(self):
        return self._payee_account_open_id

    @payee_account_open_id.setter
    def payee_account_open_id(self, value):
        self._payee_account_open_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def risk_custom_info(self):
        return self._risk_custom_info

    @risk_custom_info.setter
    def risk_custom_info(self, value):
        self._risk_custom_info = value
    @property
    def risk_trade_feedback(self):
        return self._risk_trade_feedback

    @risk_trade_feedback.setter
    def risk_trade_feedback(self, value):
        self._risk_trade_feedback = value
    @property
    def risk_trade_feedback_time(self):
        return self._risk_trade_feedback_time

    @risk_trade_feedback_time.setter
    def risk_trade_feedback_time(self, value):
        self._risk_trade_feedback_time = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payee_account_open_id:
            if hasattr(self.payee_account_open_id, 'to_alipay_dict'):
                params['payee_account_open_id'] = self.payee_account_open_id.to_alipay_dict()
            else:
                params['payee_account_open_id'] = self.payee_account_open_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.risk_custom_info:
            if hasattr(self.risk_custom_info, 'to_alipay_dict'):
                params['risk_custom_info'] = self.risk_custom_info.to_alipay_dict()
            else:
                params['risk_custom_info'] = self.risk_custom_info
        if self.risk_trade_feedback:
            if hasattr(self.risk_trade_feedback, 'to_alipay_dict'):
                params['risk_trade_feedback'] = self.risk_trade_feedback.to_alipay_dict()
            else:
                params['risk_trade_feedback'] = self.risk_trade_feedback
        if self.risk_trade_feedback_time:
            if hasattr(self.risk_trade_feedback_time, 'to_alipay_dict'):
                params['risk_trade_feedback_time'] = self.risk_trade_feedback_time.to_alipay_dict()
            else:
                params['risk_trade_feedback_time'] = self.risk_trade_feedback_time
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskJointdecisionTradeSendModel()
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payee_account_open_id' in d:
            o.payee_account_open_id = d['payee_account_open_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'risk_custom_info' in d:
            o.risk_custom_info = d['risk_custom_info']
        if 'risk_trade_feedback' in d:
            o.risk_trade_feedback = d['risk_trade_feedback']
        if 'risk_trade_feedback_time' in d:
            o.risk_trade_feedback_time = d['risk_trade_feedback_time']
        if 'scene' in d:
            o.scene = d['scene']
        if 'smid' in d:
            o.smid = d['smid']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


