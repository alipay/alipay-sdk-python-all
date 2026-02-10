#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandShopInfoBatchqueryModel(object):

    def __init__(self):
        self._address_version = None
        self._biz_source = None
        self._ip_role_id = None
        self._need_industry_info = None
        self._need_industry_license = None
        self._need_recommend = None
        self._page_num = None
        self._page_size = None
        self._shop_type = None

    @property
    def address_version(self):
        return self._address_version

    @address_version.setter
    def address_version(self, value):
        self._address_version = value
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def need_industry_info(self):
        return self._need_industry_info

    @need_industry_info.setter
    def need_industry_info(self, value):
        self._need_industry_info = value
    @property
    def need_industry_license(self):
        return self._need_industry_license

    @need_industry_license.setter
    def need_industry_license(self, value):
        self._need_industry_license = value
    @property
    def need_recommend(self):
        return self._need_recommend

    @need_recommend.setter
    def need_recommend(self, value):
        self._need_recommend = value
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
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_version:
            if hasattr(self.address_version, 'to_alipay_dict'):
                params['address_version'] = self.address_version.to_alipay_dict()
            else:
                params['address_version'] = self.address_version
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.need_industry_info:
            if hasattr(self.need_industry_info, 'to_alipay_dict'):
                params['need_industry_info'] = self.need_industry_info.to_alipay_dict()
            else:
                params['need_industry_info'] = self.need_industry_info
        if self.need_industry_license:
            if hasattr(self.need_industry_license, 'to_alipay_dict'):
                params['need_industry_license'] = self.need_industry_license.to_alipay_dict()
            else:
                params['need_industry_license'] = self.need_industry_license
        if self.need_recommend:
            if hasattr(self.need_recommend, 'to_alipay_dict'):
                params['need_recommend'] = self.need_recommend.to_alipay_dict()
            else:
                params['need_recommend'] = self.need_recommend
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
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandShopInfoBatchqueryModel()
        if 'address_version' in d:
            o.address_version = d['address_version']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'need_industry_info' in d:
            o.need_industry_info = d['need_industry_info']
        if 'need_industry_license' in d:
            o.need_industry_license = d['need_industry_license']
        if 'need_recommend' in d:
            o.need_recommend = d['need_recommend']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        return o


