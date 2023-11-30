#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetProduceItem(object):

    def __init__(self):
        self._action_type = None
        self._apply_date = None
        self._apply_order_id = None
        self._asset_pic_url = None
        self._asset_resource = None
        self._assign_item_id = None
        self._biz_line = None
        self._biz_tag = None
        self._biz_type = None
        self._city = None
        self._combination_batch_no = None
        self._combination_count = None
        self._combination_orders = None
        self._count = None
        self._create_date = None
        self._data_version = None
        self._district = None
        self._is_combination_order = None
        self._logistics_code = None
        self._logistics_name = None
        self._logistics_no = None
        self._memo = None
        self._ou_code = None
        self._ou_name = None
        self._parent_template_id = None
        self._postcode = None
        self._print_data = None
        self._priority = None
        self._produce_order = None
        self._produce_supplier_full_name = None
        self._produce_supplier_id = None
        self._produce_supplier_name = None
        self._produce_type = None
        self._province = None
        self._receiver_address = None
        self._receiver_mobile = None
        self._receiver_name = None
        self._supplier_pid = None
        self._template_id = None
        self._template_name = None
        self._work_process = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def asset_pic_url(self):
        return self._asset_pic_url

    @asset_pic_url.setter
    def asset_pic_url(self, value):
        self._asset_pic_url = value
    @property
    def asset_resource(self):
        return self._asset_resource

    @asset_resource.setter
    def asset_resource(self, value):
        self._asset_resource = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def biz_line(self):
        return self._biz_line

    @biz_line.setter
    def biz_line(self, value):
        self._biz_line = value
    @property
    def biz_tag(self):
        return self._biz_tag

    @biz_tag.setter
    def biz_tag(self, value):
        self._biz_tag = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def combination_batch_no(self):
        return self._combination_batch_no

    @combination_batch_no.setter
    def combination_batch_no(self, value):
        self._combination_batch_no = value
    @property
    def combination_count(self):
        return self._combination_count

    @combination_count.setter
    def combination_count(self, value):
        self._combination_count = value
    @property
    def combination_orders(self):
        return self._combination_orders

    @combination_orders.setter
    def combination_orders(self, value):
        if isinstance(value, list):
            self._combination_orders = list()
            for i in value:
                self._combination_orders.append(i)
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def is_combination_order(self):
        return self._is_combination_order

    @is_combination_order.setter
    def is_combination_order(self, value):
        self._is_combination_order = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def ou_name(self):
        return self._ou_name

    @ou_name.setter
    def ou_name(self, value):
        self._ou_name = value
    @property
    def parent_template_id(self):
        return self._parent_template_id

    @parent_template_id.setter
    def parent_template_id(self, value):
        self._parent_template_id = value
    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, value):
        self._postcode = value
    @property
    def print_data(self):
        return self._print_data

    @print_data.setter
    def print_data(self, value):
        self._print_data = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def produce_order(self):
        return self._produce_order

    @produce_order.setter
    def produce_order(self, value):
        self._produce_order = value
    @property
    def produce_supplier_full_name(self):
        return self._produce_supplier_full_name

    @produce_supplier_full_name.setter
    def produce_supplier_full_name(self, value):
        self._produce_supplier_full_name = value
    @property
    def produce_supplier_id(self):
        return self._produce_supplier_id

    @produce_supplier_id.setter
    def produce_supplier_id(self, value):
        self._produce_supplier_id = value
    @property
    def produce_supplier_name(self):
        return self._produce_supplier_name

    @produce_supplier_name.setter
    def produce_supplier_name(self, value):
        self._produce_supplier_name = value
    @property
    def produce_type(self):
        return self._produce_type

    @produce_type.setter
    def produce_type(self, value):
        self._produce_type = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, value):
        self._receiver_mobile = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def supplier_pid(self):
        return self._supplier_pid

    @supplier_pid.setter
    def supplier_pid(self, value):
        self._supplier_pid = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def work_process(self):
        return self._work_process

    @work_process.setter
    def work_process(self, value):
        self._work_process = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.asset_pic_url:
            if hasattr(self.asset_pic_url, 'to_alipay_dict'):
                params['asset_pic_url'] = self.asset_pic_url.to_alipay_dict()
            else:
                params['asset_pic_url'] = self.asset_pic_url
        if self.asset_resource:
            if hasattr(self.asset_resource, 'to_alipay_dict'):
                params['asset_resource'] = self.asset_resource.to_alipay_dict()
            else:
                params['asset_resource'] = self.asset_resource
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.biz_line:
            if hasattr(self.biz_line, 'to_alipay_dict'):
                params['biz_line'] = self.biz_line.to_alipay_dict()
            else:
                params['biz_line'] = self.biz_line
        if self.biz_tag:
            if hasattr(self.biz_tag, 'to_alipay_dict'):
                params['biz_tag'] = self.biz_tag.to_alipay_dict()
            else:
                params['biz_tag'] = self.biz_tag
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.combination_batch_no:
            if hasattr(self.combination_batch_no, 'to_alipay_dict'):
                params['combination_batch_no'] = self.combination_batch_no.to_alipay_dict()
            else:
                params['combination_batch_no'] = self.combination_batch_no
        if self.combination_count:
            if hasattr(self.combination_count, 'to_alipay_dict'):
                params['combination_count'] = self.combination_count.to_alipay_dict()
            else:
                params['combination_count'] = self.combination_count
        if self.combination_orders:
            if isinstance(self.combination_orders, list):
                for i in range(0, len(self.combination_orders)):
                    element = self.combination_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.combination_orders[i] = element.to_alipay_dict()
            if hasattr(self.combination_orders, 'to_alipay_dict'):
                params['combination_orders'] = self.combination_orders.to_alipay_dict()
            else:
                params['combination_orders'] = self.combination_orders
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.is_combination_order:
            if hasattr(self.is_combination_order, 'to_alipay_dict'):
                params['is_combination_order'] = self.is_combination_order.to_alipay_dict()
            else:
                params['is_combination_order'] = self.is_combination_order
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.ou_name:
            if hasattr(self.ou_name, 'to_alipay_dict'):
                params['ou_name'] = self.ou_name.to_alipay_dict()
            else:
                params['ou_name'] = self.ou_name
        if self.parent_template_id:
            if hasattr(self.parent_template_id, 'to_alipay_dict'):
                params['parent_template_id'] = self.parent_template_id.to_alipay_dict()
            else:
                params['parent_template_id'] = self.parent_template_id
        if self.postcode:
            if hasattr(self.postcode, 'to_alipay_dict'):
                params['postcode'] = self.postcode.to_alipay_dict()
            else:
                params['postcode'] = self.postcode
        if self.print_data:
            if hasattr(self.print_data, 'to_alipay_dict'):
                params['print_data'] = self.print_data.to_alipay_dict()
            else:
                params['print_data'] = self.print_data
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.produce_order:
            if hasattr(self.produce_order, 'to_alipay_dict'):
                params['produce_order'] = self.produce_order.to_alipay_dict()
            else:
                params['produce_order'] = self.produce_order
        if self.produce_supplier_full_name:
            if hasattr(self.produce_supplier_full_name, 'to_alipay_dict'):
                params['produce_supplier_full_name'] = self.produce_supplier_full_name.to_alipay_dict()
            else:
                params['produce_supplier_full_name'] = self.produce_supplier_full_name
        if self.produce_supplier_id:
            if hasattr(self.produce_supplier_id, 'to_alipay_dict'):
                params['produce_supplier_id'] = self.produce_supplier_id.to_alipay_dict()
            else:
                params['produce_supplier_id'] = self.produce_supplier_id
        if self.produce_supplier_name:
            if hasattr(self.produce_supplier_name, 'to_alipay_dict'):
                params['produce_supplier_name'] = self.produce_supplier_name.to_alipay_dict()
            else:
                params['produce_supplier_name'] = self.produce_supplier_name
        if self.produce_type:
            if hasattr(self.produce_type, 'to_alipay_dict'):
                params['produce_type'] = self.produce_type.to_alipay_dict()
            else:
                params['produce_type'] = self.produce_type
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_mobile:
            if hasattr(self.receiver_mobile, 'to_alipay_dict'):
                params['receiver_mobile'] = self.receiver_mobile.to_alipay_dict()
            else:
                params['receiver_mobile'] = self.receiver_mobile
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.supplier_pid:
            if hasattr(self.supplier_pid, 'to_alipay_dict'):
                params['supplier_pid'] = self.supplier_pid.to_alipay_dict()
            else:
                params['supplier_pid'] = self.supplier_pid
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.work_process:
            if hasattr(self.work_process, 'to_alipay_dict'):
                params['work_process'] = self.work_process.to_alipay_dict()
            else:
                params['work_process'] = self.work_process
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetProduceItem()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'asset_pic_url' in d:
            o.asset_pic_url = d['asset_pic_url']
        if 'asset_resource' in d:
            o.asset_resource = d['asset_resource']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'biz_line' in d:
            o.biz_line = d['biz_line']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'city' in d:
            o.city = d['city']
        if 'combination_batch_no' in d:
            o.combination_batch_no = d['combination_batch_no']
        if 'combination_count' in d:
            o.combination_count = d['combination_count']
        if 'combination_orders' in d:
            o.combination_orders = d['combination_orders']
        if 'count' in d:
            o.count = d['count']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'district' in d:
            o.district = d['district']
        if 'is_combination_order' in d:
            o.is_combination_order = d['is_combination_order']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'ou_name' in d:
            o.ou_name = d['ou_name']
        if 'parent_template_id' in d:
            o.parent_template_id = d['parent_template_id']
        if 'postcode' in d:
            o.postcode = d['postcode']
        if 'print_data' in d:
            o.print_data = d['print_data']
        if 'priority' in d:
            o.priority = d['priority']
        if 'produce_order' in d:
            o.produce_order = d['produce_order']
        if 'produce_supplier_full_name' in d:
            o.produce_supplier_full_name = d['produce_supplier_full_name']
        if 'produce_supplier_id' in d:
            o.produce_supplier_id = d['produce_supplier_id']
        if 'produce_supplier_name' in d:
            o.produce_supplier_name = d['produce_supplier_name']
        if 'produce_type' in d:
            o.produce_type = d['produce_type']
        if 'province' in d:
            o.province = d['province']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_mobile' in d:
            o.receiver_mobile = d['receiver_mobile']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'supplier_pid' in d:
            o.supplier_pid = d['supplier_pid']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'work_process' in d:
            o.work_process = d['work_process']
        return o


