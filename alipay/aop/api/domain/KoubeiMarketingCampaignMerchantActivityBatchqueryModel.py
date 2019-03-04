#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMerchantActivityBatchqueryModel(object):

    def __init__(self):
        self._biz_scenes = None
        self._out_request_no = None
        self._page_num = None
        self._page_size = None
        self._shop_id = None

    @property
    def biz_scenes(self):
        return self._biz_scenes

    @biz_scenes.setter
    def biz_scenes(self, value):
        if isinstance(value, list):
            self._biz_scenes = list()
            for i in value:
                self._biz_scenes.append(i)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scenes:
            if isinstance(self.biz_scenes, list):
                for i in range(0, len(self.biz_scenes)):
                    element = self.biz_scenes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_scenes[i] = element.to_alipay_dict()
            if hasattr(self.biz_scenes, 'to_alipay_dict'):
                params['biz_scenes'] = self.biz_scenes.to_alipay_dict()
            else:
                params['biz_scenes'] = self.biz_scenes
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMerchantActivityBatchqueryModel()
        if 'biz_scenes' in d:
            o.biz_scenes = d['biz_scenes']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


