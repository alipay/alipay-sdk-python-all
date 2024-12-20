#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpPaidDetailInfo import EpPaidDetailInfo
from alipay.aop.api.domain.EpPaidInDetailInfo import EpPaidInDetailInfo


class EpShareHolderInfo(object):

    def __init__(self):
        self._paid_detail = None
        self._paid_in_detail = None
        self._paid_in_money = None
        self._paid_money = None
        self._share_holder = None
        self._share_holder_type = None
        self._share_holding_ratio = None

    @property
    def paid_detail(self):
        return self._paid_detail

    @paid_detail.setter
    def paid_detail(self, value):
        if isinstance(value, EpPaidDetailInfo):
            self._paid_detail = value
        else:
            self._paid_detail = EpPaidDetailInfo.from_alipay_dict(value)
    @property
    def paid_in_detail(self):
        return self._paid_in_detail

    @paid_in_detail.setter
    def paid_in_detail(self, value):
        if isinstance(value, EpPaidInDetailInfo):
            self._paid_in_detail = value
        else:
            self._paid_in_detail = EpPaidInDetailInfo.from_alipay_dict(value)
    @property
    def paid_in_money(self):
        return self._paid_in_money

    @paid_in_money.setter
    def paid_in_money(self, value):
        self._paid_in_money = value
    @property
    def paid_money(self):
        return self._paid_money

    @paid_money.setter
    def paid_money(self, value):
        self._paid_money = value
    @property
    def share_holder(self):
        return self._share_holder

    @share_holder.setter
    def share_holder(self, value):
        self._share_holder = value
    @property
    def share_holder_type(self):
        return self._share_holder_type

    @share_holder_type.setter
    def share_holder_type(self, value):
        self._share_holder_type = value
    @property
    def share_holding_ratio(self):
        return self._share_holding_ratio

    @share_holding_ratio.setter
    def share_holding_ratio(self, value):
        self._share_holding_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.paid_detail:
            if hasattr(self.paid_detail, 'to_alipay_dict'):
                params['paid_detail'] = self.paid_detail.to_alipay_dict()
            else:
                params['paid_detail'] = self.paid_detail
        if self.paid_in_detail:
            if hasattr(self.paid_in_detail, 'to_alipay_dict'):
                params['paid_in_detail'] = self.paid_in_detail.to_alipay_dict()
            else:
                params['paid_in_detail'] = self.paid_in_detail
        if self.paid_in_money:
            if hasattr(self.paid_in_money, 'to_alipay_dict'):
                params['paid_in_money'] = self.paid_in_money.to_alipay_dict()
            else:
                params['paid_in_money'] = self.paid_in_money
        if self.paid_money:
            if hasattr(self.paid_money, 'to_alipay_dict'):
                params['paid_money'] = self.paid_money.to_alipay_dict()
            else:
                params['paid_money'] = self.paid_money
        if self.share_holder:
            if hasattr(self.share_holder, 'to_alipay_dict'):
                params['share_holder'] = self.share_holder.to_alipay_dict()
            else:
                params['share_holder'] = self.share_holder
        if self.share_holder_type:
            if hasattr(self.share_holder_type, 'to_alipay_dict'):
                params['share_holder_type'] = self.share_holder_type.to_alipay_dict()
            else:
                params['share_holder_type'] = self.share_holder_type
        if self.share_holding_ratio:
            if hasattr(self.share_holding_ratio, 'to_alipay_dict'):
                params['share_holding_ratio'] = self.share_holding_ratio.to_alipay_dict()
            else:
                params['share_holding_ratio'] = self.share_holding_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpShareHolderInfo()
        if 'paid_detail' in d:
            o.paid_detail = d['paid_detail']
        if 'paid_in_detail' in d:
            o.paid_in_detail = d['paid_in_detail']
        if 'paid_in_money' in d:
            o.paid_in_money = d['paid_in_money']
        if 'paid_money' in d:
            o.paid_money = d['paid_money']
        if 'share_holder' in d:
            o.share_holder = d['share_holder']
        if 'share_holder_type' in d:
            o.share_holder_type = d['share_holder_type']
        if 'share_holding_ratio' in d:
            o.share_holding_ratio = d['share_holding_ratio']
        return o


