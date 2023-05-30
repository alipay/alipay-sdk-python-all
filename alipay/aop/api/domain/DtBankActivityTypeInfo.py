#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankFirstBindCardGiftInfo import DtBankFirstBindCardGiftInfo
from alipay.aop.api.domain.DtBankVoucherInfo import DtBankVoucherInfo


class DtBankActivityTypeInfo(object):

    def __init__(self):
        self._activity_type = None
        self._first_bind_card_gift_info = None
        self._voucher_info = None

    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def first_bind_card_gift_info(self):
        return self._first_bind_card_gift_info

    @first_bind_card_gift_info.setter
    def first_bind_card_gift_info(self, value):
        if isinstance(value, DtBankFirstBindCardGiftInfo):
            self._first_bind_card_gift_info = value
        else:
            self._first_bind_card_gift_info = DtBankFirstBindCardGiftInfo.from_alipay_dict(value)
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, DtBankVoucherInfo):
            self._voucher_info = value
        else:
            self._voucher_info = DtBankVoucherInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.first_bind_card_gift_info:
            if hasattr(self.first_bind_card_gift_info, 'to_alipay_dict'):
                params['first_bind_card_gift_info'] = self.first_bind_card_gift_info.to_alipay_dict()
            else:
                params['first_bind_card_gift_info'] = self.first_bind_card_gift_info
        if self.voucher_info:
            if hasattr(self.voucher_info, 'to_alipay_dict'):
                params['voucher_info'] = self.voucher_info.to_alipay_dict()
            else:
                params['voucher_info'] = self.voucher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankActivityTypeInfo()
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'first_bind_card_gift_info' in d:
            o.first_bind_card_gift_info = d['first_bind_card_gift_info']
        if 'voucher_info' in d:
            o.voucher_info = d['voucher_info']
        return o


