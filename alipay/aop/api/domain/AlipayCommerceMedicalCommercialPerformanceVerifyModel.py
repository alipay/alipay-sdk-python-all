#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VerifyLogisticsDetail import VerifyLogisticsDetail


class AlipayCommerceMedicalCommercialPerformanceVerifyModel(object):

    def __init__(self):
        self._biz_order_id = None
        self._biz_url = None
        self._biz_url_type = None
        self._buyer_id = None
        self._consume_time = None
        self._open_id = None
        self._order_id = None
        self._out_biz_no = None
        self._out_product_id = None
        self._special_biz_info = None
        self._status = None
        self._total_count = None
        self._usage_count = None
        self._verify_logistics_detail = None
        self._verify_type = None

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def biz_url(self):
        return self._biz_url

    @biz_url.setter
    def biz_url(self, value):
        self._biz_url = value
    @property
    def biz_url_type(self):
        return self._biz_url_type

    @biz_url_type.setter
    def biz_url_type(self, value):
        self._biz_url_type = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def consume_time(self):
        return self._consume_time

    @consume_time.setter
    def consume_time(self, value):
        self._consume_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def special_biz_info(self):
        return self._special_biz_info

    @special_biz_info.setter
    def special_biz_info(self, value):
        self._special_biz_info = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def usage_count(self):
        return self._usage_count

    @usage_count.setter
    def usage_count(self, value):
        self._usage_count = value
    @property
    def verify_logistics_detail(self):
        return self._verify_logistics_detail

    @verify_logistics_detail.setter
    def verify_logistics_detail(self, value):
        if isinstance(value, VerifyLogisticsDetail):
            self._verify_logistics_detail = value
        else:
            self._verify_logistics_detail = VerifyLogisticsDetail.from_alipay_dict(value)
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.biz_url:
            if hasattr(self.biz_url, 'to_alipay_dict'):
                params['biz_url'] = self.biz_url.to_alipay_dict()
            else:
                params['biz_url'] = self.biz_url
        if self.biz_url_type:
            if hasattr(self.biz_url_type, 'to_alipay_dict'):
                params['biz_url_type'] = self.biz_url_type.to_alipay_dict()
            else:
                params['biz_url_type'] = self.biz_url_type
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.consume_time:
            if hasattr(self.consume_time, 'to_alipay_dict'):
                params['consume_time'] = self.consume_time.to_alipay_dict()
            else:
                params['consume_time'] = self.consume_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.special_biz_info:
            if hasattr(self.special_biz_info, 'to_alipay_dict'):
                params['special_biz_info'] = self.special_biz_info.to_alipay_dict()
            else:
                params['special_biz_info'] = self.special_biz_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.usage_count:
            if hasattr(self.usage_count, 'to_alipay_dict'):
                params['usage_count'] = self.usage_count.to_alipay_dict()
            else:
                params['usage_count'] = self.usage_count
        if self.verify_logistics_detail:
            if hasattr(self.verify_logistics_detail, 'to_alipay_dict'):
                params['verify_logistics_detail'] = self.verify_logistics_detail.to_alipay_dict()
            else:
                params['verify_logistics_detail'] = self.verify_logistics_detail
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCommercialPerformanceVerifyModel()
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'biz_url' in d:
            o.biz_url = d['biz_url']
        if 'biz_url_type' in d:
            o.biz_url_type = d['biz_url_type']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'consume_time' in d:
            o.consume_time = d['consume_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'special_biz_info' in d:
            o.special_biz_info = d['special_biz_info']
        if 'status' in d:
            o.status = d['status']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'usage_count' in d:
            o.usage_count = d['usage_count']
        if 'verify_logistics_detail' in d:
            o.verify_logistics_detail = d['verify_logistics_detail']
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        return o


