#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCreditExtInfoDTO(object):

    def __init__(self):
        self._fee_risk_model = None
        self._freeze_flag_rent_online = None
        self._pre_risk_flag_rent_online = None

    @property
    def fee_risk_model(self):
        return self._fee_risk_model

    @fee_risk_model.setter
    def fee_risk_model(self, value):
        self._fee_risk_model = value
    @property
    def freeze_flag_rent_online(self):
        return self._freeze_flag_rent_online

    @freeze_flag_rent_online.setter
    def freeze_flag_rent_online(self, value):
        self._freeze_flag_rent_online = value
    @property
    def pre_risk_flag_rent_online(self):
        return self._pre_risk_flag_rent_online

    @pre_risk_flag_rent_online.setter
    def pre_risk_flag_rent_online(self, value):
        self._pre_risk_flag_rent_online = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_risk_model:
            if hasattr(self.fee_risk_model, 'to_alipay_dict'):
                params['fee_risk_model'] = self.fee_risk_model.to_alipay_dict()
            else:
                params['fee_risk_model'] = self.fee_risk_model
        if self.freeze_flag_rent_online:
            if hasattr(self.freeze_flag_rent_online, 'to_alipay_dict'):
                params['freeze_flag_rent_online'] = self.freeze_flag_rent_online.to_alipay_dict()
            else:
                params['freeze_flag_rent_online'] = self.freeze_flag_rent_online
        if self.pre_risk_flag_rent_online:
            if hasattr(self.pre_risk_flag_rent_online, 'to_alipay_dict'):
                params['pre_risk_flag_rent_online'] = self.pre_risk_flag_rent_online.to_alipay_dict()
            else:
                params['pre_risk_flag_rent_online'] = self.pre_risk_flag_rent_online
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCreditExtInfoDTO()
        if 'fee_risk_model' in d:
            o.fee_risk_model = d['fee_risk_model']
        if 'freeze_flag_rent_online' in d:
            o.freeze_flag_rent_online = d['freeze_flag_rent_online']
        if 'pre_risk_flag_rent_online' in d:
            o.pre_risk_flag_rent_online = d['pre_risk_flag_rent_online']
        return o


