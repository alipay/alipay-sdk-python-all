#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryPackageDetail import DeliveryPackageDetail


class DeliveryPackageVO(object):

    def __init__(self):
        self._delivery_order_code = None
        self._delivery_order_id = None
        self._delivery_package_detail_list = None
        self._express_code = None
        self._gmt_create = None
        self._gmt_modified = None
        self._logistics_code = None
        self._package_code = None
        self._warehouse_code = None
        self._work_order_id = None

    @property
    def delivery_order_code(self):
        return self._delivery_order_code

    @delivery_order_code.setter
    def delivery_order_code(self, value):
        self._delivery_order_code = value
    @property
    def delivery_order_id(self):
        return self._delivery_order_id

    @delivery_order_id.setter
    def delivery_order_id(self, value):
        self._delivery_order_id = value
    @property
    def delivery_package_detail_list(self):
        return self._delivery_package_detail_list

    @delivery_package_detail_list.setter
    def delivery_package_detail_list(self, value):
        if isinstance(value, list):
            self._delivery_package_detail_list = list()
            for i in value:
                if isinstance(i, DeliveryPackageDetail):
                    self._delivery_package_detail_list.append(i)
                else:
                    self._delivery_package_detail_list.append(DeliveryPackageDetail.from_alipay_dict(i))
    @property
    def express_code(self):
        return self._express_code

    @express_code.setter
    def express_code(self, value):
        self._express_code = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value
    @property
    def work_order_id(self):
        return self._work_order_id

    @work_order_id.setter
    def work_order_id(self, value):
        self._work_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_order_code:
            if hasattr(self.delivery_order_code, 'to_alipay_dict'):
                params['delivery_order_code'] = self.delivery_order_code.to_alipay_dict()
            else:
                params['delivery_order_code'] = self.delivery_order_code
        if self.delivery_order_id:
            if hasattr(self.delivery_order_id, 'to_alipay_dict'):
                params['delivery_order_id'] = self.delivery_order_id.to_alipay_dict()
            else:
                params['delivery_order_id'] = self.delivery_order_id
        if self.delivery_package_detail_list:
            if isinstance(self.delivery_package_detail_list, list):
                for i in range(0, len(self.delivery_package_detail_list)):
                    element = self.delivery_package_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_package_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_package_detail_list, 'to_alipay_dict'):
                params['delivery_package_detail_list'] = self.delivery_package_detail_list.to_alipay_dict()
            else:
                params['delivery_package_detail_list'] = self.delivery_package_detail_list
        if self.express_code:
            if hasattr(self.express_code, 'to_alipay_dict'):
                params['express_code'] = self.express_code.to_alipay_dict()
            else:
                params['express_code'] = self.express_code
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        if self.work_order_id:
            if hasattr(self.work_order_id, 'to_alipay_dict'):
                params['work_order_id'] = self.work_order_id.to_alipay_dict()
            else:
                params['work_order_id'] = self.work_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryPackageVO()
        if 'delivery_order_code' in d:
            o.delivery_order_code = d['delivery_order_code']
        if 'delivery_order_id' in d:
            o.delivery_order_id = d['delivery_order_id']
        if 'delivery_package_detail_list' in d:
            o.delivery_package_detail_list = d['delivery_package_detail_list']
        if 'express_code' in d:
            o.express_code = d['express_code']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'package_code' in d:
            o.package_code = d['package_code']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        if 'work_order_id' in d:
            o.work_order_id = d['work_order_id']
        return o


