#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo
from alipay.aop.api.domain.PromoOperatorInfo import PromoOperatorInfo
from alipay.aop.api.domain.PromoPageInfo import PromoPageInfo


class KoubeiMarketingCampaignIntelligentPromoBatchqueryModel(object):

    def __init__(self):
        self._operator_context = None
        self._out_request_no = None
        self._owner_info = None
        self._page_info = None

    @property
    def operator_context(self):
        return self._operator_context

    @operator_context.setter
    def operator_context(self, value):
        if isinstance(value, PromoOperatorInfo):
            self._operator_context = value
        else:
            self._operator_context = PromoOperatorInfo.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def owner_info(self):
        return self._owner_info

    @owner_info.setter
    def owner_info(self, value):
        if isinstance(value, PromoOperatorInfo):
            self._owner_info = value
        else:
            self._owner_info = PromoOperatorInfo.from_alipay_dict(value)
    @property
    def page_info(self):
        return self._page_info

    @page_info.setter
    def page_info(self, value):
        if isinstance(value, PromoPageInfo):
            self._page_info = value
        else:
            self._page_info = PromoPageInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.operator_context:
            if hasattr(self.operator_context, 'to_alipay_dict'):
                params['operator_context'] = self.operator_context.to_alipay_dict()
            else:
                params['operator_context'] = self.operator_context
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.owner_info:
            if hasattr(self.owner_info, 'to_alipay_dict'):
                params['owner_info'] = self.owner_info.to_alipay_dict()
            else:
                params['owner_info'] = self.owner_info
        if self.page_info:
            if hasattr(self.page_info, 'to_alipay_dict'):
                params['page_info'] = self.page_info.to_alipay_dict()
            else:
                params['page_info'] = self.page_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignIntelligentPromoBatchqueryModel()
        if 'operator_context' in d:
            o.operator_context = d['operator_context']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'owner_info' in d:
            o.owner_info = d['owner_info']
        if 'page_info' in d:
            o.page_info = d['page_info']
        return o


