#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Appinfos import Appinfos


class StoreInfo(object):

    def __init__(self):
        self._alipay_brand_id = None
        self._alipay_shop_id = None
        self._app_infos = None
        self._biz_code = None
        self._biz_type = None
        self._ext = None
        self._fliggy_poi_id = None
        self._mini_app_desc = None
        self._mini_app_name = None
        self._seller_id = None
        self._seller_nick = None
        self._store_id = None
        self._store_status = None
        self._sub_seller_id = None

    @property
    def alipay_brand_id(self):
        return self._alipay_brand_id

    @alipay_brand_id.setter
    def alipay_brand_id(self, value):
        self._alipay_brand_id = value
    @property
    def alipay_shop_id(self):
        return self._alipay_shop_id

    @alipay_shop_id.setter
    def alipay_shop_id(self, value):
        self._alipay_shop_id = value
    @property
    def app_infos(self):
        return self._app_infos

    @app_infos.setter
    def app_infos(self, value):
        if isinstance(value, Appinfos):
            self._app_infos = value
        else:
            self._app_infos = Appinfos.from_alipay_dict(value)
    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def fliggy_poi_id(self):
        return self._fliggy_poi_id

    @fliggy_poi_id.setter
    def fliggy_poi_id(self, value):
        self._fliggy_poi_id = value
    @property
    def mini_app_desc(self):
        return self._mini_app_desc

    @mini_app_desc.setter
    def mini_app_desc(self, value):
        self._mini_app_desc = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_nick(self):
        return self._seller_nick

    @seller_nick.setter
    def seller_nick(self, value):
        self._seller_nick = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_status(self):
        return self._store_status

    @store_status.setter
    def store_status(self, value):
        self._store_status = value
    @property
    def sub_seller_id(self):
        return self._sub_seller_id

    @sub_seller_id.setter
    def sub_seller_id(self, value):
        self._sub_seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_brand_id:
            if hasattr(self.alipay_brand_id, 'to_alipay_dict'):
                params['alipay_brand_id'] = self.alipay_brand_id.to_alipay_dict()
            else:
                params['alipay_brand_id'] = self.alipay_brand_id
        if self.alipay_shop_id:
            if hasattr(self.alipay_shop_id, 'to_alipay_dict'):
                params['alipay_shop_id'] = self.alipay_shop_id.to_alipay_dict()
            else:
                params['alipay_shop_id'] = self.alipay_shop_id
        if self.app_infos:
            if hasattr(self.app_infos, 'to_alipay_dict'):
                params['app_infos'] = self.app_infos.to_alipay_dict()
            else:
                params['app_infos'] = self.app_infos
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.fliggy_poi_id:
            if hasattr(self.fliggy_poi_id, 'to_alipay_dict'):
                params['fliggy_poi_id'] = self.fliggy_poi_id.to_alipay_dict()
            else:
                params['fliggy_poi_id'] = self.fliggy_poi_id
        if self.mini_app_desc:
            if hasattr(self.mini_app_desc, 'to_alipay_dict'):
                params['mini_app_desc'] = self.mini_app_desc.to_alipay_dict()
            else:
                params['mini_app_desc'] = self.mini_app_desc
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_nick:
            if hasattr(self.seller_nick, 'to_alipay_dict'):
                params['seller_nick'] = self.seller_nick.to_alipay_dict()
            else:
                params['seller_nick'] = self.seller_nick
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_status:
            if hasattr(self.store_status, 'to_alipay_dict'):
                params['store_status'] = self.store_status.to_alipay_dict()
            else:
                params['store_status'] = self.store_status
        if self.sub_seller_id:
            if hasattr(self.sub_seller_id, 'to_alipay_dict'):
                params['sub_seller_id'] = self.sub_seller_id.to_alipay_dict()
            else:
                params['sub_seller_id'] = self.sub_seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StoreInfo()
        if 'alipay_brand_id' in d:
            o.alipay_brand_id = d['alipay_brand_id']
        if 'alipay_shop_id' in d:
            o.alipay_shop_id = d['alipay_shop_id']
        if 'app_infos' in d:
            o.app_infos = d['app_infos']
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ext' in d:
            o.ext = d['ext']
        if 'fliggy_poi_id' in d:
            o.fliggy_poi_id = d['fliggy_poi_id']
        if 'mini_app_desc' in d:
            o.mini_app_desc = d['mini_app_desc']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_nick' in d:
            o.seller_nick = d['seller_nick']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_status' in d:
            o.store_status = d['store_status']
        if 'sub_seller_id' in d:
            o.sub_seller_id = d['sub_seller_id']
        return o


