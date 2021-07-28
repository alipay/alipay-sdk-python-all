#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncPriceAutoCreateModel(object):

    def __init__(self):
        self._app_name = None
        self._biz_unit_code = None
        self._commodity_code = None
        self._commodity_name = None
        self._commodity_version = None
        self._creator_id = None
        self._creator_nm = None
        self._gmt_invalid = None
        self._gmt_valid = None
        self._inst_id = None
        self._memo = None
        self._out_biz_no = None
        self._price_name = None
        self._price_origin = None
        self._price_tpl_id = None
        self._price_tpl_version = None
        self._tnt_inst_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def biz_unit_code(self):
        return self._biz_unit_code

    @biz_unit_code.setter
    def biz_unit_code(self, value):
        self._biz_unit_code = value
    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def commodity_name(self):
        return self._commodity_name

    @commodity_name.setter
    def commodity_name(self, value):
        self._commodity_name = value
    @property
    def commodity_version(self):
        return self._commodity_version

    @commodity_version.setter
    def commodity_version(self, value):
        self._commodity_version = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_nm(self):
        return self._creator_nm

    @creator_nm.setter
    def creator_nm(self, value):
        self._creator_nm = value
    @property
    def gmt_invalid(self):
        return self._gmt_invalid

    @gmt_invalid.setter
    def gmt_invalid(self, value):
        self._gmt_invalid = value
    @property
    def gmt_valid(self):
        return self._gmt_valid

    @gmt_valid.setter
    def gmt_valid(self, value):
        self._gmt_valid = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def price_name(self):
        return self._price_name

    @price_name.setter
    def price_name(self, value):
        self._price_name = value
    @property
    def price_origin(self):
        return self._price_origin

    @price_origin.setter
    def price_origin(self, value):
        self._price_origin = value
    @property
    def price_tpl_id(self):
        return self._price_tpl_id

    @price_tpl_id.setter
    def price_tpl_id(self, value):
        self._price_tpl_id = value
    @property
    def price_tpl_version(self):
        return self._price_tpl_version

    @price_tpl_version.setter
    def price_tpl_version(self, value):
        self._price_tpl_version = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.biz_unit_code:
            if hasattr(self.biz_unit_code, 'to_alipay_dict'):
                params['biz_unit_code'] = self.biz_unit_code.to_alipay_dict()
            else:
                params['biz_unit_code'] = self.biz_unit_code
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.commodity_name:
            if hasattr(self.commodity_name, 'to_alipay_dict'):
                params['commodity_name'] = self.commodity_name.to_alipay_dict()
            else:
                params['commodity_name'] = self.commodity_name
        if self.commodity_version:
            if hasattr(self.commodity_version, 'to_alipay_dict'):
                params['commodity_version'] = self.commodity_version.to_alipay_dict()
            else:
                params['commodity_version'] = self.commodity_version
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_nm:
            if hasattr(self.creator_nm, 'to_alipay_dict'):
                params['creator_nm'] = self.creator_nm.to_alipay_dict()
            else:
                params['creator_nm'] = self.creator_nm
        if self.gmt_invalid:
            if hasattr(self.gmt_invalid, 'to_alipay_dict'):
                params['gmt_invalid'] = self.gmt_invalid.to_alipay_dict()
            else:
                params['gmt_invalid'] = self.gmt_invalid
        if self.gmt_valid:
            if hasattr(self.gmt_valid, 'to_alipay_dict'):
                params['gmt_valid'] = self.gmt_valid.to_alipay_dict()
            else:
                params['gmt_valid'] = self.gmt_valid
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.price_name:
            if hasattr(self.price_name, 'to_alipay_dict'):
                params['price_name'] = self.price_name.to_alipay_dict()
            else:
                params['price_name'] = self.price_name
        if self.price_origin:
            if hasattr(self.price_origin, 'to_alipay_dict'):
                params['price_origin'] = self.price_origin.to_alipay_dict()
            else:
                params['price_origin'] = self.price_origin
        if self.price_tpl_id:
            if hasattr(self.price_tpl_id, 'to_alipay_dict'):
                params['price_tpl_id'] = self.price_tpl_id.to_alipay_dict()
            else:
                params['price_tpl_id'] = self.price_tpl_id
        if self.price_tpl_version:
            if hasattr(self.price_tpl_version, 'to_alipay_dict'):
                params['price_tpl_version'] = self.price_tpl_version.to_alipay_dict()
            else:
                params['price_tpl_version'] = self.price_tpl_version
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncPriceAutoCreateModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_unit_code' in d:
            o.biz_unit_code = d['biz_unit_code']
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'commodity_name' in d:
            o.commodity_name = d['commodity_name']
        if 'commodity_version' in d:
            o.commodity_version = d['commodity_version']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_nm' in d:
            o.creator_nm = d['creator_nm']
        if 'gmt_invalid' in d:
            o.gmt_invalid = d['gmt_invalid']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'price_name' in d:
            o.price_name = d['price_name']
        if 'price_origin' in d:
            o.price_origin = d['price_origin']
        if 'price_tpl_id' in d:
            o.price_tpl_id = d['price_tpl_id']
        if 'price_tpl_version' in d:
            o.price_tpl_version = d['price_tpl_version']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


