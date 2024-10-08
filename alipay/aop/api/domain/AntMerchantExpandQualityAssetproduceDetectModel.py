#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.QualityDetectDetail import QualityDetectDetail


class AntMerchantExpandQualityAssetproduceDetectModel(object):

    def __init__(self):
        self._amount = None
        self._assign_item_id = None
        self._quality_detect_detail = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def quality_detect_detail(self):
        return self._quality_detect_detail

    @quality_detect_detail.setter
    def quality_detect_detail(self, value):
        if isinstance(value, list):
            self._quality_detect_detail = list()
            for i in value:
                if isinstance(i, QualityDetectDetail):
                    self._quality_detect_detail.append(i)
                else:
                    self._quality_detect_detail.append(QualityDetectDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.quality_detect_detail:
            if isinstance(self.quality_detect_detail, list):
                for i in range(0, len(self.quality_detect_detail)):
                    element = self.quality_detect_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quality_detect_detail[i] = element.to_alipay_dict()
            if hasattr(self.quality_detect_detail, 'to_alipay_dict'):
                params['quality_detect_detail'] = self.quality_detect_detail.to_alipay_dict()
            else:
                params['quality_detect_detail'] = self.quality_detect_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandQualityAssetproduceDetectModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'quality_detect_detail' in d:
            o.quality_detect_detail = d['quality_detect_detail']
        return o


