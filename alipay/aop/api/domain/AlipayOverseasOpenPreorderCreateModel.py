#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionISVAgentInfoDTO import TuitionISVAgentInfoDTO
from alipay.aop.api.domain.TuitionISVPayerInfoDTO import TuitionISVPayerInfoDTO
from alipay.aop.api.domain.TuitionISVRequestPaymentInfoDTO import TuitionISVRequestPaymentInfoDTO
from alipay.aop.api.domain.TuitionISVStudentInfoDTO import TuitionISVStudentInfoDTO


class AlipayOverseasOpenPreorderCreateModel(object):

    def __init__(self):
        self._agent_info = None
        self._finish_self_audit = None
        self._payer_info = None
        self._payment_info = None
        self._pre_order_id = None
        self._student_info = None

    @property
    def agent_info(self):
        return self._agent_info

    @agent_info.setter
    def agent_info(self, value):
        if isinstance(value, TuitionISVAgentInfoDTO):
            self._agent_info = value
        else:
            self._agent_info = TuitionISVAgentInfoDTO.from_alipay_dict(value)
    @property
    def finish_self_audit(self):
        return self._finish_self_audit

    @finish_self_audit.setter
    def finish_self_audit(self, value):
        self._finish_self_audit = value
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, TuitionISVPayerInfoDTO):
            self._payer_info = value
        else:
            self._payer_info = TuitionISVPayerInfoDTO.from_alipay_dict(value)
    @property
    def payment_info(self):
        return self._payment_info

    @payment_info.setter
    def payment_info(self, value):
        if isinstance(value, TuitionISVRequestPaymentInfoDTO):
            self._payment_info = value
        else:
            self._payment_info = TuitionISVRequestPaymentInfoDTO.from_alipay_dict(value)
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def student_info(self):
        return self._student_info

    @student_info.setter
    def student_info(self, value):
        if isinstance(value, TuitionISVStudentInfoDTO):
            self._student_info = value
        else:
            self._student_info = TuitionISVStudentInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agent_info:
            if hasattr(self.agent_info, 'to_alipay_dict'):
                params['agent_info'] = self.agent_info.to_alipay_dict()
            else:
                params['agent_info'] = self.agent_info
        if self.finish_self_audit:
            if hasattr(self.finish_self_audit, 'to_alipay_dict'):
                params['finish_self_audit'] = self.finish_self_audit.to_alipay_dict()
            else:
                params['finish_self_audit'] = self.finish_self_audit
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.payment_info:
            if hasattr(self.payment_info, 'to_alipay_dict'):
                params['payment_info'] = self.payment_info.to_alipay_dict()
            else:
                params['payment_info'] = self.payment_info
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        if self.student_info:
            if hasattr(self.student_info, 'to_alipay_dict'):
                params['student_info'] = self.student_info.to_alipay_dict()
            else:
                params['student_info'] = self.student_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenPreorderCreateModel()
        if 'agent_info' in d:
            o.agent_info = d['agent_info']
        if 'finish_self_audit' in d:
            o.finish_self_audit = d['finish_self_audit']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'payment_info' in d:
            o.payment_info = d['payment_info']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        if 'student_info' in d:
            o.student_info = d['student_info']
        return o


