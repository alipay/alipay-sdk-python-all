#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentProcurementReceiverInfoDTO(object):

    def __init__(self):
        self._receiver_id_card_no = None

    @property
    def receiver_id_card_no(self):
        return self._receiver_id_card_no

    @receiver_id_card_no.setter
    def receiver_id_card_no(self, value):
        self._receiver_id_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.receiver_id_card_no:
            if hasattr(self.receiver_id_card_no, 'to_alipay_dict'):
                params['receiver_id_card_no'] = self.receiver_id_card_no.to_alipay_dict()
            else:
                params['receiver_id_card_no'] = self.receiver_id_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentProcurementReceiverInfoDTO()
        if 'receiver_id_card_no' in d:
            o.receiver_id_card_no = d['receiver_id_card_no']
        return o


