#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherExpressInfo import VoucherExpressInfo
from alipay.aop.api.domain.VoucherGoodsQuantitySpecificationInfo import VoucherGoodsQuantitySpecificationInfo


class VoucherDeductThresholdInfo(object):

    def __init__(self):
        self._customer_define_voucher_threshold_desc = None
        self._voucher_express_info = None
        self._voucher_goods_quantity_specification_info = None

    @property
    def customer_define_voucher_threshold_desc(self):
        return self._customer_define_voucher_threshold_desc

    @customer_define_voucher_threshold_desc.setter
    def customer_define_voucher_threshold_desc(self, value):
        self._customer_define_voucher_threshold_desc = value
    @property
    def voucher_express_info(self):
        return self._voucher_express_info

    @voucher_express_info.setter
    def voucher_express_info(self, value):
        if isinstance(value, VoucherExpressInfo):
            self._voucher_express_info = value
        else:
            self._voucher_express_info = VoucherExpressInfo.from_alipay_dict(value)
    @property
    def voucher_goods_quantity_specification_info(self):
        return self._voucher_goods_quantity_specification_info

    @voucher_goods_quantity_specification_info.setter
    def voucher_goods_quantity_specification_info(self, value):
        if isinstance(value, VoucherGoodsQuantitySpecificationInfo):
            self._voucher_goods_quantity_specification_info = value
        else:
            self._voucher_goods_quantity_specification_info = VoucherGoodsQuantitySpecificationInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.customer_define_voucher_threshold_desc:
            if hasattr(self.customer_define_voucher_threshold_desc, 'to_alipay_dict'):
                params['customer_define_voucher_threshold_desc'] = self.customer_define_voucher_threshold_desc.to_alipay_dict()
            else:
                params['customer_define_voucher_threshold_desc'] = self.customer_define_voucher_threshold_desc
        if self.voucher_express_info:
            if hasattr(self.voucher_express_info, 'to_alipay_dict'):
                params['voucher_express_info'] = self.voucher_express_info.to_alipay_dict()
            else:
                params['voucher_express_info'] = self.voucher_express_info
        if self.voucher_goods_quantity_specification_info:
            if hasattr(self.voucher_goods_quantity_specification_info, 'to_alipay_dict'):
                params['voucher_goods_quantity_specification_info'] = self.voucher_goods_quantity_specification_info.to_alipay_dict()
            else:
                params['voucher_goods_quantity_specification_info'] = self.voucher_goods_quantity_specification_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherDeductThresholdInfo()
        if 'customer_define_voucher_threshold_desc' in d:
            o.customer_define_voucher_threshold_desc = d['customer_define_voucher_threshold_desc']
        if 'voucher_express_info' in d:
            o.voucher_express_info = d['voucher_express_info']
        if 'voucher_goods_quantity_specification_info' in d:
            o.voucher_goods_quantity_specification_info = d['voucher_goods_quantity_specification_info']
        return o


