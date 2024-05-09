#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgOrderExtInfo import MsgOrderExtInfo
from alipay.aop.api.domain.MsgOrderGoodsInfoList import MsgOrderGoodsInfoList


class AlipayEcoCityserviceMessageOrderCreateModel(object):

    def __init__(self):
        self._app_code = None
        self._certificate_number = None
        self._city_code = None
        self._encrypt_type = None
        self._ext_info = None
        self._goods_info_list = None
        self._industry_id = None
        self._mobile = None
        self._open_id = None
        self._order_amount = None
        self._order_create_time = None
        self._order_update_time = None
        self._out_order_no = None
        self._pay_amount = None
        self._scene_type = None
        self._status = None
        self._target_url = None
        self._template_id = None
        self._user_id = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, MsgOrderExtInfo):
            self._ext_info = value
        else:
            self._ext_info = MsgOrderExtInfo.from_alipay_dict(value)
    @property
    def goods_info_list(self):
        return self._goods_info_list

    @goods_info_list.setter
    def goods_info_list(self, value):
        if isinstance(value, list):
            self._goods_info_list = list()
            for i in value:
                if isinstance(i, MsgOrderGoodsInfoList):
                    self._goods_info_list.append(i)
                else:
                    self._goods_info_list.append(MsgOrderGoodsInfoList.from_alipay_dict(i))
    @property
    def industry_id(self):
        return self._industry_id

    @industry_id.setter
    def industry_id(self, value):
        self._industry_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
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
    def order_update_time(self):
        return self._order_update_time

    @order_update_time.setter
    def order_update_time(self, value):
        self._order_update_time = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_info_list:
            if isinstance(self.goods_info_list, list):
                for i in range(0, len(self.goods_info_list)):
                    element = self.goods_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_info_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_info_list, 'to_alipay_dict'):
                params['goods_info_list'] = self.goods_info_list.to_alipay_dict()
            else:
                params['goods_info_list'] = self.goods_info_list
        if self.industry_id:
            if hasattr(self.industry_id, 'to_alipay_dict'):
                params['industry_id'] = self.industry_id.to_alipay_dict()
            else:
                params['industry_id'] = self.industry_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        if self.order_update_time:
            if hasattr(self.order_update_time, 'to_alipay_dict'):
                params['order_update_time'] = self.order_update_time.to_alipay_dict()
            else:
                params['order_update_time'] = self.order_update_time
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceMessageOrderCreateModel()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_info_list' in d:
            o.goods_info_list = d['goods_info_list']
        if 'industry_id' in d:
            o.industry_id = d['industry_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_update_time' in d:
            o.order_update_time = d['order_update_time']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'status' in d:
            o.status = d['status']
        if 'target_url' in d:
            o.target_url = d['target_url']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


