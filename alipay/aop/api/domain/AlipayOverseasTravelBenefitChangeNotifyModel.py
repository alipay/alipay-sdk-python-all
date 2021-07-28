#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitDetailInfo import BenefitDetailInfo


class AlipayOverseasTravelBenefitChangeNotifyModel(object):

    def __init__(self):
        self._acquirer_id = None
        self._benefit_detail_info_list = None
        self._psp_id = None

    @property
    def acquirer_id(self):
        return self._acquirer_id

    @acquirer_id.setter
    def acquirer_id(self, value):
        self._acquirer_id = value
    @property
    def benefit_detail_info_list(self):
        return self._benefit_detail_info_list

    @benefit_detail_info_list.setter
    def benefit_detail_info_list(self, value):
        if isinstance(value, list):
            self._benefit_detail_info_list = list()
            for i in value:
                if isinstance(i, BenefitDetailInfo):
                    self._benefit_detail_info_list.append(i)
                else:
                    self._benefit_detail_info_list.append(BenefitDetailInfo.from_alipay_dict(i))
    @property
    def psp_id(self):
        return self._psp_id

    @psp_id.setter
    def psp_id(self, value):
        self._psp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquirer_id:
            if hasattr(self.acquirer_id, 'to_alipay_dict'):
                params['acquirer_id'] = self.acquirer_id.to_alipay_dict()
            else:
                params['acquirer_id'] = self.acquirer_id
        if self.benefit_detail_info_list:
            if isinstance(self.benefit_detail_info_list, list):
                for i in range(0, len(self.benefit_detail_info_list)):
                    element = self.benefit_detail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_detail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.benefit_detail_info_list, 'to_alipay_dict'):
                params['benefit_detail_info_list'] = self.benefit_detail_info_list.to_alipay_dict()
            else:
                params['benefit_detail_info_list'] = self.benefit_detail_info_list
        if self.psp_id:
            if hasattr(self.psp_id, 'to_alipay_dict'):
                params['psp_id'] = self.psp_id.to_alipay_dict()
            else:
                params['psp_id'] = self.psp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelBenefitChangeNotifyModel()
        if 'acquirer_id' in d:
            o.acquirer_id = d['acquirer_id']
        if 'benefit_detail_info_list' in d:
            o.benefit_detail_info_list = d['benefit_detail_info_list']
        if 'psp_id' in d:
            o.psp_id = d['psp_id']
        return o


