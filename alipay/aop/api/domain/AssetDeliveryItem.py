#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CCInfo import CCInfo
from alipay.aop.api.domain.AssetDeliveryAddress import AssetDeliveryAddress
from alipay.aop.api.domain.LogisticsInfo import LogisticsInfo
from alipay.aop.api.domain.AssetDeliveryAddress import AssetDeliveryAddress


class AssetDeliveryItem(object):

    def __init__(self):
        self._action_type = None
        self._amount = None
        self._apply_order_date = None
        self._apply_order_id = None
        self._assign_item_id = None
        self._assign_out_order_id = None
        self._biz_line = None
        self._biz_tag = None
        self._biz_type = None
        self._custom_clearance = None
        self._delivery_assign_order_item_id = None
        self._delivery_process_no = None
        self._delivery_process_supplier_id = None
        self._delivery_process_supplier_name = None
        self._delivery_supplier_full_name = None
        self._delivery_supplier_id = None
        self._delivery_supplier_name = None
        self._ext_info = None
        self._from_address = None
        self._gmt_assign = None
        self._item_id = None
        self._item_name = None
        self._logistics_info = None
        self._memo = None
        self._operate_info = None
        self._ou_code = None
        self._ou_name = None
        self._out_biz_no = None
        self._parent_item_id = None
        self._print_data = None
        self._produce_order_item_id = None
        self._record_type = None
        self._supplier_id = None
        self._supplier_name = None
        self._to_address = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def apply_order_date(self):
        return self._apply_order_date

    @apply_order_date.setter
    def apply_order_date(self, value):
        self._apply_order_date = value
    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def assign_out_order_id(self):
        return self._assign_out_order_id

    @assign_out_order_id.setter
    def assign_out_order_id(self, value):
        self._assign_out_order_id = value
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
    def custom_clearance(self):
        return self._custom_clearance

    @custom_clearance.setter
    def custom_clearance(self, value):
        if isinstance(value, CCInfo):
            self._custom_clearance = value
        else:
            self._custom_clearance = CCInfo.from_alipay_dict(value)
    @property
    def delivery_assign_order_item_id(self):
        return self._delivery_assign_order_item_id

    @delivery_assign_order_item_id.setter
    def delivery_assign_order_item_id(self, value):
        self._delivery_assign_order_item_id = value
    @property
    def delivery_process_no(self):
        return self._delivery_process_no

    @delivery_process_no.setter
    def delivery_process_no(self, value):
        self._delivery_process_no = value
    @property
    def delivery_process_supplier_id(self):
        return self._delivery_process_supplier_id

    @delivery_process_supplier_id.setter
    def delivery_process_supplier_id(self, value):
        self._delivery_process_supplier_id = value
    @property
    def delivery_process_supplier_name(self):
        return self._delivery_process_supplier_name

    @delivery_process_supplier_name.setter
    def delivery_process_supplier_name(self, value):
        self._delivery_process_supplier_name = value
    @property
    def delivery_supplier_full_name(self):
        return self._delivery_supplier_full_name

    @delivery_supplier_full_name.setter
    def delivery_supplier_full_name(self, value):
        self._delivery_supplier_full_name = value
    @property
    def delivery_supplier_id(self):
        return self._delivery_supplier_id

    @delivery_supplier_id.setter
    def delivery_supplier_id(self, value):
        self._delivery_supplier_id = value
    @property
    def delivery_supplier_name(self):
        return self._delivery_supplier_name

    @delivery_supplier_name.setter
    def delivery_supplier_name(self, value):
        self._delivery_supplier_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def from_address(self):
        return self._from_address

    @from_address.setter
    def from_address(self, value):
        if isinstance(value, AssetDeliveryAddress):
            self._from_address = value
        else:
            self._from_address = AssetDeliveryAddress.from_alipay_dict(value)
    @property
    def gmt_assign(self):
        return self._gmt_assign

    @gmt_assign.setter
    def gmt_assign(self, value):
        self._gmt_assign = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, LogisticsInfo):
            self._logistics_info = value
        else:
            self._logistics_info = LogisticsInfo.from_alipay_dict(value)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operate_info(self):
        return self._operate_info

    @operate_info.setter
    def operate_info(self, value):
        self._operate_info = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def parent_item_id(self):
        return self._parent_item_id

    @parent_item_id.setter
    def parent_item_id(self, value):
        self._parent_item_id = value
    @property
    def print_data(self):
        return self._print_data

    @print_data.setter
    def print_data(self, value):
        self._print_data = value
    @property
    def produce_order_item_id(self):
        return self._produce_order_item_id

    @produce_order_item_id.setter
    def produce_order_item_id(self, value):
        self._produce_order_item_id = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value
    @property
    def to_address(self):
        return self._to_address

    @to_address.setter
    def to_address(self, value):
        if isinstance(value, AssetDeliveryAddress):
            self._to_address = value
        else:
            self._to_address = AssetDeliveryAddress.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.apply_order_date:
            if hasattr(self.apply_order_date, 'to_alipay_dict'):
                params['apply_order_date'] = self.apply_order_date.to_alipay_dict()
            else:
                params['apply_order_date'] = self.apply_order_date
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.assign_out_order_id:
            if hasattr(self.assign_out_order_id, 'to_alipay_dict'):
                params['assign_out_order_id'] = self.assign_out_order_id.to_alipay_dict()
            else:
                params['assign_out_order_id'] = self.assign_out_order_id
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
        if self.custom_clearance:
            if hasattr(self.custom_clearance, 'to_alipay_dict'):
                params['custom_clearance'] = self.custom_clearance.to_alipay_dict()
            else:
                params['custom_clearance'] = self.custom_clearance
        if self.delivery_assign_order_item_id:
            if hasattr(self.delivery_assign_order_item_id, 'to_alipay_dict'):
                params['delivery_assign_order_item_id'] = self.delivery_assign_order_item_id.to_alipay_dict()
            else:
                params['delivery_assign_order_item_id'] = self.delivery_assign_order_item_id
        if self.delivery_process_no:
            if hasattr(self.delivery_process_no, 'to_alipay_dict'):
                params['delivery_process_no'] = self.delivery_process_no.to_alipay_dict()
            else:
                params['delivery_process_no'] = self.delivery_process_no
        if self.delivery_process_supplier_id:
            if hasattr(self.delivery_process_supplier_id, 'to_alipay_dict'):
                params['delivery_process_supplier_id'] = self.delivery_process_supplier_id.to_alipay_dict()
            else:
                params['delivery_process_supplier_id'] = self.delivery_process_supplier_id
        if self.delivery_process_supplier_name:
            if hasattr(self.delivery_process_supplier_name, 'to_alipay_dict'):
                params['delivery_process_supplier_name'] = self.delivery_process_supplier_name.to_alipay_dict()
            else:
                params['delivery_process_supplier_name'] = self.delivery_process_supplier_name
        if self.delivery_supplier_full_name:
            if hasattr(self.delivery_supplier_full_name, 'to_alipay_dict'):
                params['delivery_supplier_full_name'] = self.delivery_supplier_full_name.to_alipay_dict()
            else:
                params['delivery_supplier_full_name'] = self.delivery_supplier_full_name
        if self.delivery_supplier_id:
            if hasattr(self.delivery_supplier_id, 'to_alipay_dict'):
                params['delivery_supplier_id'] = self.delivery_supplier_id.to_alipay_dict()
            else:
                params['delivery_supplier_id'] = self.delivery_supplier_id
        if self.delivery_supplier_name:
            if hasattr(self.delivery_supplier_name, 'to_alipay_dict'):
                params['delivery_supplier_name'] = self.delivery_supplier_name.to_alipay_dict()
            else:
                params['delivery_supplier_name'] = self.delivery_supplier_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.from_address:
            if hasattr(self.from_address, 'to_alipay_dict'):
                params['from_address'] = self.from_address.to_alipay_dict()
            else:
                params['from_address'] = self.from_address
        if self.gmt_assign:
            if hasattr(self.gmt_assign, 'to_alipay_dict'):
                params['gmt_assign'] = self.gmt_assign.to_alipay_dict()
            else:
                params['gmt_assign'] = self.gmt_assign
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.logistics_info:
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operate_info:
            if hasattr(self.operate_info, 'to_alipay_dict'):
                params['operate_info'] = self.operate_info.to_alipay_dict()
            else:
                params['operate_info'] = self.operate_info
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.parent_item_id:
            if hasattr(self.parent_item_id, 'to_alipay_dict'):
                params['parent_item_id'] = self.parent_item_id.to_alipay_dict()
            else:
                params['parent_item_id'] = self.parent_item_id
        if self.print_data:
            if hasattr(self.print_data, 'to_alipay_dict'):
                params['print_data'] = self.print_data.to_alipay_dict()
            else:
                params['print_data'] = self.print_data
        if self.produce_order_item_id:
            if hasattr(self.produce_order_item_id, 'to_alipay_dict'):
                params['produce_order_item_id'] = self.produce_order_item_id.to_alipay_dict()
            else:
                params['produce_order_item_id'] = self.produce_order_item_id
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
        if self.to_address:
            if hasattr(self.to_address, 'to_alipay_dict'):
                params['to_address'] = self.to_address.to_alipay_dict()
            else:
                params['to_address'] = self.to_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetDeliveryItem()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'amount' in d:
            o.amount = d['amount']
        if 'apply_order_date' in d:
            o.apply_order_date = d['apply_order_date']
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'assign_out_order_id' in d:
            o.assign_out_order_id = d['assign_out_order_id']
        if 'biz_line' in d:
            o.biz_line = d['biz_line']
        if 'biz_tag' in d:
            o.biz_tag = d['biz_tag']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'custom_clearance' in d:
            o.custom_clearance = d['custom_clearance']
        if 'delivery_assign_order_item_id' in d:
            o.delivery_assign_order_item_id = d['delivery_assign_order_item_id']
        if 'delivery_process_no' in d:
            o.delivery_process_no = d['delivery_process_no']
        if 'delivery_process_supplier_id' in d:
            o.delivery_process_supplier_id = d['delivery_process_supplier_id']
        if 'delivery_process_supplier_name' in d:
            o.delivery_process_supplier_name = d['delivery_process_supplier_name']
        if 'delivery_supplier_full_name' in d:
            o.delivery_supplier_full_name = d['delivery_supplier_full_name']
        if 'delivery_supplier_id' in d:
            o.delivery_supplier_id = d['delivery_supplier_id']
        if 'delivery_supplier_name' in d:
            o.delivery_supplier_name = d['delivery_supplier_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'from_address' in d:
            o.from_address = d['from_address']
        if 'gmt_assign' in d:
            o.gmt_assign = d['gmt_assign']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operate_info' in d:
            o.operate_info = d['operate_info']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'ou_name' in d:
            o.ou_name = d['ou_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'parent_item_id' in d:
            o.parent_item_id = d['parent_item_id']
        if 'print_data' in d:
            o.print_data = d['print_data']
        if 'produce_order_item_id' in d:
            o.produce_order_item_id = d['produce_order_item_id']
        if 'record_type' in d:
            o.record_type = d['record_type']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        if 'to_address' in d:
            o.to_address = d['to_address']
        return o


