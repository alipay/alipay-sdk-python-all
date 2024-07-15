#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BpmsMessageDTO import BpmsMessageDTO


class AlipayBossFncBpmsMessageTransferModel(object):

    def __init__(self):
        self._bpms_message_dto = None

    @property
    def bpms_message_dto(self):
        return self._bpms_message_dto

    @bpms_message_dto.setter
    def bpms_message_dto(self, value):
        if isinstance(value, BpmsMessageDTO):
            self._bpms_message_dto = value
        else:
            self._bpms_message_dto = BpmsMessageDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bpms_message_dto:
            if hasattr(self.bpms_message_dto, 'to_alipay_dict'):
                params['bpms_message_dto'] = self.bpms_message_dto.to_alipay_dict()
            else:
                params['bpms_message_dto'] = self.bpms_message_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncBpmsMessageTransferModel()
        if 'bpms_message_dto' in d:
            o.bpms_message_dto = d['bpms_message_dto']
        return o


