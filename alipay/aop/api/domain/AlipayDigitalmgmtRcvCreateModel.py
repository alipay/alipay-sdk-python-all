#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcvCreateDto import RcvCreateDto


class AlipayDigitalmgmtRcvCreateModel(object):

    def __init__(self):
        self._rcv_create_dto = None

    @property
    def rcv_create_dto(self):
        return self._rcv_create_dto

    @rcv_create_dto.setter
    def rcv_create_dto(self, value):
        if isinstance(value, RcvCreateDto):
            self._rcv_create_dto = value
        else:
            self._rcv_create_dto = RcvCreateDto.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.rcv_create_dto:
            if hasattr(self.rcv_create_dto, 'to_alipay_dict'):
                params['rcv_create_dto'] = self.rcv_create_dto.to_alipay_dict()
            else:
                params['rcv_create_dto'] = self.rcv_create_dto
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtRcvCreateModel()
        if 'rcv_create_dto' in d:
            o.rcv_create_dto = d['rcv_create_dto']
        return o


