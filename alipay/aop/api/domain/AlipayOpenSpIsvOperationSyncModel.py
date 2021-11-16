#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationResultExtInfo import OperationResultExtInfo


class AlipayOpenSpIsvOperationSyncModel(object):

    def __init__(self):
        self._customer_type = None
        self._ext_info = None
        self._implement_end_time = None
        self._implement_object_name = None
        self._implement_place = None
        self._implement_result = None
        self._implement_result_image = None
        self._implement_result_remark = None
        self._implement_start_time = None
        self._item_code = None
        self._item_price = None
        self._merchant_pid = None
        self._mini_appid = None
        self._oppor_id = None
        self._order_id = None
        self._out_biz_no = None
        self._promotor_pid = None
        self._shop_id = None
        self._sub_promotor_pid = None

    @property
    def customer_type(self):
        return self._customer_type

    @customer_type.setter
    def customer_type(self, value):
        self._customer_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, OperationResultExtInfo):
            self._ext_info = value
        else:
            self._ext_info = OperationResultExtInfo.from_alipay_dict(value)
    @property
    def implement_end_time(self):
        return self._implement_end_time

    @implement_end_time.setter
    def implement_end_time(self, value):
        self._implement_end_time = value
    @property
    def implement_object_name(self):
        return self._implement_object_name

    @implement_object_name.setter
    def implement_object_name(self, value):
        self._implement_object_name = value
    @property
    def implement_place(self):
        return self._implement_place

    @implement_place.setter
    def implement_place(self, value):
        self._implement_place = value
    @property
    def implement_result(self):
        return self._implement_result

    @implement_result.setter
    def implement_result(self, value):
        self._implement_result = value
    @property
    def implement_result_image(self):
        return self._implement_result_image

    @implement_result_image.setter
    def implement_result_image(self, value):
        self._implement_result_image = value
    @property
    def implement_result_remark(self):
        return self._implement_result_remark

    @implement_result_remark.setter
    def implement_result_remark(self, value):
        self._implement_result_remark = value
    @property
    def implement_start_time(self):
        return self._implement_start_time

    @implement_start_time.setter
    def implement_start_time(self, value):
        self._implement_start_time = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mini_appid(self):
        return self._mini_appid

    @mini_appid.setter
    def mini_appid(self, value):
        self._mini_appid = value
    @property
    def oppor_id(self):
        return self._oppor_id

    @oppor_id.setter
    def oppor_id(self, value):
        self._oppor_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def promotor_pid(self):
        return self._promotor_pid

    @promotor_pid.setter
    def promotor_pid(self, value):
        self._promotor_pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sub_promotor_pid(self):
        return self._sub_promotor_pid

    @sub_promotor_pid.setter
    def sub_promotor_pid(self, value):
        self._sub_promotor_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_type:
            if hasattr(self.customer_type, 'to_alipay_dict'):
                params['customer_type'] = self.customer_type.to_alipay_dict()
            else:
                params['customer_type'] = self.customer_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.implement_end_time:
            if hasattr(self.implement_end_time, 'to_alipay_dict'):
                params['implement_end_time'] = self.implement_end_time.to_alipay_dict()
            else:
                params['implement_end_time'] = self.implement_end_time
        if self.implement_object_name:
            if hasattr(self.implement_object_name, 'to_alipay_dict'):
                params['implement_object_name'] = self.implement_object_name.to_alipay_dict()
            else:
                params['implement_object_name'] = self.implement_object_name
        if self.implement_place:
            if hasattr(self.implement_place, 'to_alipay_dict'):
                params['implement_place'] = self.implement_place.to_alipay_dict()
            else:
                params['implement_place'] = self.implement_place
        if self.implement_result:
            if hasattr(self.implement_result, 'to_alipay_dict'):
                params['implement_result'] = self.implement_result.to_alipay_dict()
            else:
                params['implement_result'] = self.implement_result
        if self.implement_result_image:
            if hasattr(self.implement_result_image, 'to_alipay_dict'):
                params['implement_result_image'] = self.implement_result_image.to_alipay_dict()
            else:
                params['implement_result_image'] = self.implement_result_image
        if self.implement_result_remark:
            if hasattr(self.implement_result_remark, 'to_alipay_dict'):
                params['implement_result_remark'] = self.implement_result_remark.to_alipay_dict()
            else:
                params['implement_result_remark'] = self.implement_result_remark
        if self.implement_start_time:
            if hasattr(self.implement_start_time, 'to_alipay_dict'):
                params['implement_start_time'] = self.implement_start_time.to_alipay_dict()
            else:
                params['implement_start_time'] = self.implement_start_time
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mini_appid:
            if hasattr(self.mini_appid, 'to_alipay_dict'):
                params['mini_appid'] = self.mini_appid.to_alipay_dict()
            else:
                params['mini_appid'] = self.mini_appid
        if self.oppor_id:
            if hasattr(self.oppor_id, 'to_alipay_dict'):
                params['oppor_id'] = self.oppor_id.to_alipay_dict()
            else:
                params['oppor_id'] = self.oppor_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.promotor_pid:
            if hasattr(self.promotor_pid, 'to_alipay_dict'):
                params['promotor_pid'] = self.promotor_pid.to_alipay_dict()
            else:
                params['promotor_pid'] = self.promotor_pid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sub_promotor_pid:
            if hasattr(self.sub_promotor_pid, 'to_alipay_dict'):
                params['sub_promotor_pid'] = self.sub_promotor_pid.to_alipay_dict()
            else:
                params['sub_promotor_pid'] = self.sub_promotor_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpIsvOperationSyncModel()
        if 'customer_type' in d:
            o.customer_type = d['customer_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'implement_end_time' in d:
            o.implement_end_time = d['implement_end_time']
        if 'implement_object_name' in d:
            o.implement_object_name = d['implement_object_name']
        if 'implement_place' in d:
            o.implement_place = d['implement_place']
        if 'implement_result' in d:
            o.implement_result = d['implement_result']
        if 'implement_result_image' in d:
            o.implement_result_image = d['implement_result_image']
        if 'implement_result_remark' in d:
            o.implement_result_remark = d['implement_result_remark']
        if 'implement_start_time' in d:
            o.implement_start_time = d['implement_start_time']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'mini_appid' in d:
            o.mini_appid = d['mini_appid']
        if 'oppor_id' in d:
            o.oppor_id = d['oppor_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'promotor_pid' in d:
            o.promotor_pid = d['promotor_pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sub_promotor_pid' in d:
            o.sub_promotor_pid = d['sub_promotor_pid']
        return o


