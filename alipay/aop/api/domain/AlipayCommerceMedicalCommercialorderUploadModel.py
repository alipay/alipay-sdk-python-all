#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalCommercialOrderUploadExtInfo import MedicalCommercialOrderUploadExtInfo


class AlipayCommerceMedicalCommercialorderUploadModel(object):

    def __init__(self):
        self._actual_amount = None
        self._alipay_trade_no = None
        self._buyer_open_id = None
        self._buyer_uid = None
        self._ext_info = None
        self._goods_app_code = None
        self._goods_desc = None
        self._goods_name = None
        self._merchant_order_detail_url = None
        self._order_amount = None
        self._order_create_time = None
        self._order_modified_time = None
        self._order_status = None
        self._order_type = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._out_goods_id = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def buyer_uid(self):
        return self._buyer_uid

    @buyer_uid.setter
    def buyer_uid(self, value):
        self._buyer_uid = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, MedicalCommercialOrderUploadExtInfo):
            self._ext_info = value
        else:
            self._ext_info = MedicalCommercialOrderUploadExtInfo.from_alipay_dict(value)
    @property
    def goods_app_code(self):
        return self._goods_app_code

    @goods_app_code.setter
    def goods_app_code(self, value):
        self._goods_app_code = value
    @property
    def goods_desc(self):
        return self._goods_desc

    @goods_desc.setter
    def goods_desc(self, value):
        self._goods_desc = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def merchant_order_detail_url(self):
        return self._merchant_order_detail_url

    @merchant_order_detail_url.setter
    def merchant_order_detail_url(self, value):
        self._merchant_order_detail_url = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def out_goods_id(self):
        return self._out_goods_id

    @out_goods_id.setter
    def out_goods_id(self, value):
        self._out_goods_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.buyer_uid:
            if hasattr(self.buyer_uid, 'to_alipay_dict'):
                params['buyer_uid'] = self.buyer_uid.to_alipay_dict()
            else:
                params['buyer_uid'] = self.buyer_uid
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_app_code:
            if hasattr(self.goods_app_code, 'to_alipay_dict'):
                params['goods_app_code'] = self.goods_app_code.to_alipay_dict()
            else:
                params['goods_app_code'] = self.goods_app_code
        if self.goods_desc:
            if hasattr(self.goods_desc, 'to_alipay_dict'):
                params['goods_desc'] = self.goods_desc.to_alipay_dict()
            else:
                params['goods_desc'] = self.goods_desc
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.merchant_order_detail_url:
            if hasattr(self.merchant_order_detail_url, 'to_alipay_dict'):
                params['merchant_order_detail_url'] = self.merchant_order_detail_url.to_alipay_dict()
            else:
                params['merchant_order_detail_url'] = self.merchant_order_detail_url
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.out_goods_id:
            if hasattr(self.out_goods_id, 'to_alipay_dict'):
                params['out_goods_id'] = self.out_goods_id.to_alipay_dict()
            else:
                params['out_goods_id'] = self.out_goods_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCommercialorderUploadModel()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'buyer_uid' in d:
            o.buyer_uid = d['buyer_uid']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_app_code' in d:
            o.goods_app_code = d['goods_app_code']
        if 'goods_desc' in d:
            o.goods_desc = d['goods_desc']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'merchant_order_detail_url' in d:
            o.merchant_order_detail_url = d['merchant_order_detail_url']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'out_goods_id' in d:
            o.out_goods_id = d['out_goods_id']
        return o


