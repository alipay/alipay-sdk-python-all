#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PtcNewGoodsApplyRequestVo(object):

    def __init__(self):
        self._algorithm_id = None
        self._apply_id = None
        self._apply_open_id = None
        self._apply_status = None
        self._apply_user = None
        self._business_source = None
        self._category = None
        self._deleted = None
        self._depth = None
        self._entity_audit_open_id = None
        self._entity_audit_time = None
        self._entity_audit_user = None
        self._express_number = None
        self._finish_open_id = None
        self._finish_time = None
        self._finish_user = None
        self._franchisee_id = None
        self._goods_big_type = None
        self._goods_id = None
        self._goods_name = None
        self._goods_small_type = None
        self._goods_upc = None
        self._height = None
        self._id = None
        self._img_info = None
        self._info_audit_open_id = None
        self._info_audit_time = None
        self._info_audit_user = None
        self._low_weight_goods = None
        self._main_algorithm_id = None
        self._merchant_app_id = None
        self._merchant_pid = None
        self._new_goods_apply_type = None
        self._pack_type = None
        self._phone = None
        self._purchase_link = None
        self._reject_msg = None
        self._repeat_algorithm_id = None
        self._repeat_goods_code = None
        self._sample_weight = None
        self._sell_goods_type = None
        self._standard_goods = None
        self._standard_saleable_goods = None
        self._transport_type = None
        self._weight_goods = None
        self._width = None

    @property
    def algorithm_id(self):
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, value):
        self._algorithm_id = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_open_id(self):
        return self._apply_open_id

    @apply_open_id.setter
    def apply_open_id(self, value):
        self._apply_open_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def apply_user(self):
        return self._apply_user

    @apply_user.setter
    def apply_user(self, value):
        self._apply_user = value
    @property
    def business_source(self):
        return self._business_source

    @business_source.setter
    def business_source(self, value):
        self._business_source = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, value):
        self._deleted = value
    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value
    @property
    def entity_audit_open_id(self):
        return self._entity_audit_open_id

    @entity_audit_open_id.setter
    def entity_audit_open_id(self, value):
        self._entity_audit_open_id = value
    @property
    def entity_audit_time(self):
        return self._entity_audit_time

    @entity_audit_time.setter
    def entity_audit_time(self, value):
        self._entity_audit_time = value
    @property
    def entity_audit_user(self):
        return self._entity_audit_user

    @entity_audit_user.setter
    def entity_audit_user(self, value):
        self._entity_audit_user = value
    @property
    def express_number(self):
        return self._express_number

    @express_number.setter
    def express_number(self, value):
        self._express_number = value
    @property
    def finish_open_id(self):
        return self._finish_open_id

    @finish_open_id.setter
    def finish_open_id(self, value):
        self._finish_open_id = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def finish_user(self):
        return self._finish_user

    @finish_user.setter
    def finish_user(self, value):
        self._finish_user = value
    @property
    def franchisee_id(self):
        return self._franchisee_id

    @franchisee_id.setter
    def franchisee_id(self, value):
        self._franchisee_id = value
    @property
    def goods_big_type(self):
        return self._goods_big_type

    @goods_big_type.setter
    def goods_big_type(self, value):
        self._goods_big_type = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def goods_small_type(self):
        return self._goods_small_type

    @goods_small_type.setter
    def goods_small_type(self, value):
        self._goods_small_type = value
    @property
    def goods_upc(self):
        return self._goods_upc

    @goods_upc.setter
    def goods_upc(self, value):
        self._goods_upc = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def img_info(self):
        return self._img_info

    @img_info.setter
    def img_info(self, value):
        self._img_info = value
    @property
    def info_audit_open_id(self):
        return self._info_audit_open_id

    @info_audit_open_id.setter
    def info_audit_open_id(self, value):
        self._info_audit_open_id = value
    @property
    def info_audit_time(self):
        return self._info_audit_time

    @info_audit_time.setter
    def info_audit_time(self, value):
        self._info_audit_time = value
    @property
    def info_audit_user(self):
        return self._info_audit_user

    @info_audit_user.setter
    def info_audit_user(self, value):
        self._info_audit_user = value
    @property
    def low_weight_goods(self):
        return self._low_weight_goods

    @low_weight_goods.setter
    def low_weight_goods(self, value):
        self._low_weight_goods = value
    @property
    def main_algorithm_id(self):
        return self._main_algorithm_id

    @main_algorithm_id.setter
    def main_algorithm_id(self, value):
        self._main_algorithm_id = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def new_goods_apply_type(self):
        return self._new_goods_apply_type

    @new_goods_apply_type.setter
    def new_goods_apply_type(self, value):
        self._new_goods_apply_type = value
    @property
    def pack_type(self):
        return self._pack_type

    @pack_type.setter
    def pack_type(self, value):
        self._pack_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def purchase_link(self):
        return self._purchase_link

    @purchase_link.setter
    def purchase_link(self, value):
        self._purchase_link = value
    @property
    def reject_msg(self):
        return self._reject_msg

    @reject_msg.setter
    def reject_msg(self, value):
        self._reject_msg = value
    @property
    def repeat_algorithm_id(self):
        return self._repeat_algorithm_id

    @repeat_algorithm_id.setter
    def repeat_algorithm_id(self, value):
        self._repeat_algorithm_id = value
    @property
    def repeat_goods_code(self):
        return self._repeat_goods_code

    @repeat_goods_code.setter
    def repeat_goods_code(self, value):
        self._repeat_goods_code = value
    @property
    def sample_weight(self):
        return self._sample_weight

    @sample_weight.setter
    def sample_weight(self, value):
        self._sample_weight = value
    @property
    def sell_goods_type(self):
        return self._sell_goods_type

    @sell_goods_type.setter
    def sell_goods_type(self, value):
        self._sell_goods_type = value
    @property
    def standard_goods(self):
        return self._standard_goods

    @standard_goods.setter
    def standard_goods(self, value):
        self._standard_goods = value
    @property
    def standard_saleable_goods(self):
        return self._standard_saleable_goods

    @standard_saleable_goods.setter
    def standard_saleable_goods(self, value):
        self._standard_saleable_goods = value
    @property
    def transport_type(self):
        return self._transport_type

    @transport_type.setter
    def transport_type(self, value):
        self._transport_type = value
    @property
    def weight_goods(self):
        return self._weight_goods

    @weight_goods.setter
    def weight_goods(self, value):
        self._weight_goods = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_id:
            if hasattr(self.algorithm_id, 'to_alipay_dict'):
                params['algorithm_id'] = self.algorithm_id.to_alipay_dict()
            else:
                params['algorithm_id'] = self.algorithm_id
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_open_id:
            if hasattr(self.apply_open_id, 'to_alipay_dict'):
                params['apply_open_id'] = self.apply_open_id.to_alipay_dict()
            else:
                params['apply_open_id'] = self.apply_open_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.apply_user:
            if hasattr(self.apply_user, 'to_alipay_dict'):
                params['apply_user'] = self.apply_user.to_alipay_dict()
            else:
                params['apply_user'] = self.apply_user
        if self.business_source:
            if hasattr(self.business_source, 'to_alipay_dict'):
                params['business_source'] = self.business_source.to_alipay_dict()
            else:
                params['business_source'] = self.business_source
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.deleted:
            if hasattr(self.deleted, 'to_alipay_dict'):
                params['deleted'] = self.deleted.to_alipay_dict()
            else:
                params['deleted'] = self.deleted
        if self.depth:
            if hasattr(self.depth, 'to_alipay_dict'):
                params['depth'] = self.depth.to_alipay_dict()
            else:
                params['depth'] = self.depth
        if self.entity_audit_open_id:
            if hasattr(self.entity_audit_open_id, 'to_alipay_dict'):
                params['entity_audit_open_id'] = self.entity_audit_open_id.to_alipay_dict()
            else:
                params['entity_audit_open_id'] = self.entity_audit_open_id
        if self.entity_audit_time:
            if hasattr(self.entity_audit_time, 'to_alipay_dict'):
                params['entity_audit_time'] = self.entity_audit_time.to_alipay_dict()
            else:
                params['entity_audit_time'] = self.entity_audit_time
        if self.entity_audit_user:
            if hasattr(self.entity_audit_user, 'to_alipay_dict'):
                params['entity_audit_user'] = self.entity_audit_user.to_alipay_dict()
            else:
                params['entity_audit_user'] = self.entity_audit_user
        if self.express_number:
            if hasattr(self.express_number, 'to_alipay_dict'):
                params['express_number'] = self.express_number.to_alipay_dict()
            else:
                params['express_number'] = self.express_number
        if self.finish_open_id:
            if hasattr(self.finish_open_id, 'to_alipay_dict'):
                params['finish_open_id'] = self.finish_open_id.to_alipay_dict()
            else:
                params['finish_open_id'] = self.finish_open_id
        if self.finish_time:
            if hasattr(self.finish_time, 'to_alipay_dict'):
                params['finish_time'] = self.finish_time.to_alipay_dict()
            else:
                params['finish_time'] = self.finish_time
        if self.finish_user:
            if hasattr(self.finish_user, 'to_alipay_dict'):
                params['finish_user'] = self.finish_user.to_alipay_dict()
            else:
                params['finish_user'] = self.finish_user
        if self.franchisee_id:
            if hasattr(self.franchisee_id, 'to_alipay_dict'):
                params['franchisee_id'] = self.franchisee_id.to_alipay_dict()
            else:
                params['franchisee_id'] = self.franchisee_id
        if self.goods_big_type:
            if hasattr(self.goods_big_type, 'to_alipay_dict'):
                params['goods_big_type'] = self.goods_big_type.to_alipay_dict()
            else:
                params['goods_big_type'] = self.goods_big_type
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.goods_small_type:
            if hasattr(self.goods_small_type, 'to_alipay_dict'):
                params['goods_small_type'] = self.goods_small_type.to_alipay_dict()
            else:
                params['goods_small_type'] = self.goods_small_type
        if self.goods_upc:
            if hasattr(self.goods_upc, 'to_alipay_dict'):
                params['goods_upc'] = self.goods_upc.to_alipay_dict()
            else:
                params['goods_upc'] = self.goods_upc
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.img_info:
            if hasattr(self.img_info, 'to_alipay_dict'):
                params['img_info'] = self.img_info.to_alipay_dict()
            else:
                params['img_info'] = self.img_info
        if self.info_audit_open_id:
            if hasattr(self.info_audit_open_id, 'to_alipay_dict'):
                params['info_audit_open_id'] = self.info_audit_open_id.to_alipay_dict()
            else:
                params['info_audit_open_id'] = self.info_audit_open_id
        if self.info_audit_time:
            if hasattr(self.info_audit_time, 'to_alipay_dict'):
                params['info_audit_time'] = self.info_audit_time.to_alipay_dict()
            else:
                params['info_audit_time'] = self.info_audit_time
        if self.info_audit_user:
            if hasattr(self.info_audit_user, 'to_alipay_dict'):
                params['info_audit_user'] = self.info_audit_user.to_alipay_dict()
            else:
                params['info_audit_user'] = self.info_audit_user
        if self.low_weight_goods:
            if hasattr(self.low_weight_goods, 'to_alipay_dict'):
                params['low_weight_goods'] = self.low_weight_goods.to_alipay_dict()
            else:
                params['low_weight_goods'] = self.low_weight_goods
        if self.main_algorithm_id:
            if hasattr(self.main_algorithm_id, 'to_alipay_dict'):
                params['main_algorithm_id'] = self.main_algorithm_id.to_alipay_dict()
            else:
                params['main_algorithm_id'] = self.main_algorithm_id
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.new_goods_apply_type:
            if hasattr(self.new_goods_apply_type, 'to_alipay_dict'):
                params['new_goods_apply_type'] = self.new_goods_apply_type.to_alipay_dict()
            else:
                params['new_goods_apply_type'] = self.new_goods_apply_type
        if self.pack_type:
            if hasattr(self.pack_type, 'to_alipay_dict'):
                params['pack_type'] = self.pack_type.to_alipay_dict()
            else:
                params['pack_type'] = self.pack_type
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.purchase_link:
            if hasattr(self.purchase_link, 'to_alipay_dict'):
                params['purchase_link'] = self.purchase_link.to_alipay_dict()
            else:
                params['purchase_link'] = self.purchase_link
        if self.reject_msg:
            if hasattr(self.reject_msg, 'to_alipay_dict'):
                params['reject_msg'] = self.reject_msg.to_alipay_dict()
            else:
                params['reject_msg'] = self.reject_msg
        if self.repeat_algorithm_id:
            if hasattr(self.repeat_algorithm_id, 'to_alipay_dict'):
                params['repeat_algorithm_id'] = self.repeat_algorithm_id.to_alipay_dict()
            else:
                params['repeat_algorithm_id'] = self.repeat_algorithm_id
        if self.repeat_goods_code:
            if hasattr(self.repeat_goods_code, 'to_alipay_dict'):
                params['repeat_goods_code'] = self.repeat_goods_code.to_alipay_dict()
            else:
                params['repeat_goods_code'] = self.repeat_goods_code
        if self.sample_weight:
            if hasattr(self.sample_weight, 'to_alipay_dict'):
                params['sample_weight'] = self.sample_weight.to_alipay_dict()
            else:
                params['sample_weight'] = self.sample_weight
        if self.sell_goods_type:
            if hasattr(self.sell_goods_type, 'to_alipay_dict'):
                params['sell_goods_type'] = self.sell_goods_type.to_alipay_dict()
            else:
                params['sell_goods_type'] = self.sell_goods_type
        if self.standard_goods:
            if hasattr(self.standard_goods, 'to_alipay_dict'):
                params['standard_goods'] = self.standard_goods.to_alipay_dict()
            else:
                params['standard_goods'] = self.standard_goods
        if self.standard_saleable_goods:
            if hasattr(self.standard_saleable_goods, 'to_alipay_dict'):
                params['standard_saleable_goods'] = self.standard_saleable_goods.to_alipay_dict()
            else:
                params['standard_saleable_goods'] = self.standard_saleable_goods
        if self.transport_type:
            if hasattr(self.transport_type, 'to_alipay_dict'):
                params['transport_type'] = self.transport_type.to_alipay_dict()
            else:
                params['transport_type'] = self.transport_type
        if self.weight_goods:
            if hasattr(self.weight_goods, 'to_alipay_dict'):
                params['weight_goods'] = self.weight_goods.to_alipay_dict()
            else:
                params['weight_goods'] = self.weight_goods
        if self.width:
            if hasattr(self.width, 'to_alipay_dict'):
                params['width'] = self.width.to_alipay_dict()
            else:
                params['width'] = self.width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PtcNewGoodsApplyRequestVo()
        if 'algorithm_id' in d:
            o.algorithm_id = d['algorithm_id']
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_open_id' in d:
            o.apply_open_id = d['apply_open_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'apply_user' in d:
            o.apply_user = d['apply_user']
        if 'business_source' in d:
            o.business_source = d['business_source']
        if 'category' in d:
            o.category = d['category']
        if 'deleted' in d:
            o.deleted = d['deleted']
        if 'depth' in d:
            o.depth = d['depth']
        if 'entity_audit_open_id' in d:
            o.entity_audit_open_id = d['entity_audit_open_id']
        if 'entity_audit_time' in d:
            o.entity_audit_time = d['entity_audit_time']
        if 'entity_audit_user' in d:
            o.entity_audit_user = d['entity_audit_user']
        if 'express_number' in d:
            o.express_number = d['express_number']
        if 'finish_open_id' in d:
            o.finish_open_id = d['finish_open_id']
        if 'finish_time' in d:
            o.finish_time = d['finish_time']
        if 'finish_user' in d:
            o.finish_user = d['finish_user']
        if 'franchisee_id' in d:
            o.franchisee_id = d['franchisee_id']
        if 'goods_big_type' in d:
            o.goods_big_type = d['goods_big_type']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'goods_small_type' in d:
            o.goods_small_type = d['goods_small_type']
        if 'goods_upc' in d:
            o.goods_upc = d['goods_upc']
        if 'height' in d:
            o.height = d['height']
        if 'id' in d:
            o.id = d['id']
        if 'img_info' in d:
            o.img_info = d['img_info']
        if 'info_audit_open_id' in d:
            o.info_audit_open_id = d['info_audit_open_id']
        if 'info_audit_time' in d:
            o.info_audit_time = d['info_audit_time']
        if 'info_audit_user' in d:
            o.info_audit_user = d['info_audit_user']
        if 'low_weight_goods' in d:
            o.low_weight_goods = d['low_weight_goods']
        if 'main_algorithm_id' in d:
            o.main_algorithm_id = d['main_algorithm_id']
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'new_goods_apply_type' in d:
            o.new_goods_apply_type = d['new_goods_apply_type']
        if 'pack_type' in d:
            o.pack_type = d['pack_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'purchase_link' in d:
            o.purchase_link = d['purchase_link']
        if 'reject_msg' in d:
            o.reject_msg = d['reject_msg']
        if 'repeat_algorithm_id' in d:
            o.repeat_algorithm_id = d['repeat_algorithm_id']
        if 'repeat_goods_code' in d:
            o.repeat_goods_code = d['repeat_goods_code']
        if 'sample_weight' in d:
            o.sample_weight = d['sample_weight']
        if 'sell_goods_type' in d:
            o.sell_goods_type = d['sell_goods_type']
        if 'standard_goods' in d:
            o.standard_goods = d['standard_goods']
        if 'standard_saleable_goods' in d:
            o.standard_saleable_goods = d['standard_saleable_goods']
        if 'transport_type' in d:
            o.transport_type = d['transport_type']
        if 'weight_goods' in d:
            o.weight_goods = d['weight_goods']
        if 'width' in d:
            o.width = d['width']
        return o


