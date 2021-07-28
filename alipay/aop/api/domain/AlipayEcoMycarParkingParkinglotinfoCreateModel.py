#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessItem import BusinessItem


class AlipayEcoMycarParkingParkinglotinfoCreateModel(object):

    def __init__(self):
        self._agent_id = None
        self._business_isv = None
        self._city_id = None
        self._contact_alipay = None
        self._contact_emali = None
        self._contact_mobile = None
        self._contact_name = None
        self._contact_tel = None
        self._contact_weixin = None
        self._equipment_name = None
        self._is_support_invoice = None
        self._isv_mobile = None
        self._latitude = None
        self._longitude = None
        self._mchnt_id = None
        self._original_isv_appid = None
        self._original_isv_mobile = None
        self._original_isv_name = None
        self._original_isv_pid = None
        self._out_parking_id = None
        self._parking_address = None
        self._parking_end_time = None
        self._parking_fee_description = None
        self._parking_fee_description_img = None
        self._parking_lot_type = None
        self._parking_mobile = None
        self._parking_name = None
        self._parking_number = None
        self._parking_poiid = None
        self._parking_start_time = None
        self._parking_type = None
        self._pay_type = None
        self._payment_mode = None
        self._shopingmall_id = None
        self._sum_space = None
        self._support_after_pay = None
        self._time_out = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def business_isv(self):
        return self._business_isv

    @business_isv.setter
    def business_isv(self, value):
        if isinstance(value, list):
            self._business_isv = list()
            for i in value:
                if isinstance(i, BusinessItem):
                    self._business_isv.append(i)
                else:
                    self._business_isv.append(BusinessItem.from_alipay_dict(i))
    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def contact_alipay(self):
        return self._contact_alipay

    @contact_alipay.setter
    def contact_alipay(self, value):
        self._contact_alipay = value
    @property
    def contact_emali(self):
        return self._contact_emali

    @contact_emali.setter
    def contact_emali(self, value):
        self._contact_emali = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_tel(self):
        return self._contact_tel

    @contact_tel.setter
    def contact_tel(self, value):
        self._contact_tel = value
    @property
    def contact_weixin(self):
        return self._contact_weixin

    @contact_weixin.setter
    def contact_weixin(self, value):
        self._contact_weixin = value
    @property
    def equipment_name(self):
        return self._equipment_name

    @equipment_name.setter
    def equipment_name(self, value):
        self._equipment_name = value
    @property
    def is_support_invoice(self):
        return self._is_support_invoice

    @is_support_invoice.setter
    def is_support_invoice(self, value):
        self._is_support_invoice = value
    @property
    def isv_mobile(self):
        return self._isv_mobile

    @isv_mobile.setter
    def isv_mobile(self, value):
        self._isv_mobile = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mchnt_id(self):
        return self._mchnt_id

    @mchnt_id.setter
    def mchnt_id(self, value):
        self._mchnt_id = value
    @property
    def original_isv_appid(self):
        return self._original_isv_appid

    @original_isv_appid.setter
    def original_isv_appid(self, value):
        self._original_isv_appid = value
    @property
    def original_isv_mobile(self):
        return self._original_isv_mobile

    @original_isv_mobile.setter
    def original_isv_mobile(self, value):
        self._original_isv_mobile = value
    @property
    def original_isv_name(self):
        return self._original_isv_name

    @original_isv_name.setter
    def original_isv_name(self, value):
        self._original_isv_name = value
    @property
    def original_isv_pid(self):
        return self._original_isv_pid

    @original_isv_pid.setter
    def original_isv_pid(self, value):
        self._original_isv_pid = value
    @property
    def out_parking_id(self):
        return self._out_parking_id

    @out_parking_id.setter
    def out_parking_id(self, value):
        self._out_parking_id = value
    @property
    def parking_address(self):
        return self._parking_address

    @parking_address.setter
    def parking_address(self, value):
        self._parking_address = value
    @property
    def parking_end_time(self):
        return self._parking_end_time

    @parking_end_time.setter
    def parking_end_time(self, value):
        self._parking_end_time = value
    @property
    def parking_fee_description(self):
        return self._parking_fee_description

    @parking_fee_description.setter
    def parking_fee_description(self, value):
        self._parking_fee_description = value
    @property
    def parking_fee_description_img(self):
        return self._parking_fee_description_img

    @parking_fee_description_img.setter
    def parking_fee_description_img(self, value):
        self._parking_fee_description_img = value
    @property
    def parking_lot_type(self):
        return self._parking_lot_type

    @parking_lot_type.setter
    def parking_lot_type(self, value):
        self._parking_lot_type = value
    @property
    def parking_mobile(self):
        return self._parking_mobile

    @parking_mobile.setter
    def parking_mobile(self, value):
        self._parking_mobile = value
    @property
    def parking_name(self):
        return self._parking_name

    @parking_name.setter
    def parking_name(self, value):
        self._parking_name = value
    @property
    def parking_number(self):
        return self._parking_number

    @parking_number.setter
    def parking_number(self, value):
        self._parking_number = value
    @property
    def parking_poiid(self):
        return self._parking_poiid

    @parking_poiid.setter
    def parking_poiid(self, value):
        self._parking_poiid = value
    @property
    def parking_start_time(self):
        return self._parking_start_time

    @parking_start_time.setter
    def parking_start_time(self, value):
        self._parking_start_time = value
    @property
    def parking_type(self):
        return self._parking_type

    @parking_type.setter
    def parking_type(self, value):
        self._parking_type = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def payment_mode(self):
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, value):
        self._payment_mode = value
    @property
    def shopingmall_id(self):
        return self._shopingmall_id

    @shopingmall_id.setter
    def shopingmall_id(self, value):
        self._shopingmall_id = value
    @property
    def sum_space(self):
        return self._sum_space

    @sum_space.setter
    def sum_space(self, value):
        self._sum_space = value
    @property
    def support_after_pay(self):
        return self._support_after_pay

    @support_after_pay.setter
    def support_after_pay(self, value):
        self._support_after_pay = value
    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, value):
        self._time_out = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.business_isv:
            if isinstance(self.business_isv, list):
                for i in range(0, len(self.business_isv)):
                    element = self.business_isv[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_isv[i] = element.to_alipay_dict()
            if hasattr(self.business_isv, 'to_alipay_dict'):
                params['business_isv'] = self.business_isv.to_alipay_dict()
            else:
                params['business_isv'] = self.business_isv
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.contact_alipay:
            if hasattr(self.contact_alipay, 'to_alipay_dict'):
                params['contact_alipay'] = self.contact_alipay.to_alipay_dict()
            else:
                params['contact_alipay'] = self.contact_alipay
        if self.contact_emali:
            if hasattr(self.contact_emali, 'to_alipay_dict'):
                params['contact_emali'] = self.contact_emali.to_alipay_dict()
            else:
                params['contact_emali'] = self.contact_emali
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_tel:
            if hasattr(self.contact_tel, 'to_alipay_dict'):
                params['contact_tel'] = self.contact_tel.to_alipay_dict()
            else:
                params['contact_tel'] = self.contact_tel
        if self.contact_weixin:
            if hasattr(self.contact_weixin, 'to_alipay_dict'):
                params['contact_weixin'] = self.contact_weixin.to_alipay_dict()
            else:
                params['contact_weixin'] = self.contact_weixin
        if self.equipment_name:
            if hasattr(self.equipment_name, 'to_alipay_dict'):
                params['equipment_name'] = self.equipment_name.to_alipay_dict()
            else:
                params['equipment_name'] = self.equipment_name
        if self.is_support_invoice:
            if hasattr(self.is_support_invoice, 'to_alipay_dict'):
                params['is_support_invoice'] = self.is_support_invoice.to_alipay_dict()
            else:
                params['is_support_invoice'] = self.is_support_invoice
        if self.isv_mobile:
            if hasattr(self.isv_mobile, 'to_alipay_dict'):
                params['isv_mobile'] = self.isv_mobile.to_alipay_dict()
            else:
                params['isv_mobile'] = self.isv_mobile
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mchnt_id:
            if hasattr(self.mchnt_id, 'to_alipay_dict'):
                params['mchnt_id'] = self.mchnt_id.to_alipay_dict()
            else:
                params['mchnt_id'] = self.mchnt_id
        if self.original_isv_appid:
            if hasattr(self.original_isv_appid, 'to_alipay_dict'):
                params['original_isv_appid'] = self.original_isv_appid.to_alipay_dict()
            else:
                params['original_isv_appid'] = self.original_isv_appid
        if self.original_isv_mobile:
            if hasattr(self.original_isv_mobile, 'to_alipay_dict'):
                params['original_isv_mobile'] = self.original_isv_mobile.to_alipay_dict()
            else:
                params['original_isv_mobile'] = self.original_isv_mobile
        if self.original_isv_name:
            if hasattr(self.original_isv_name, 'to_alipay_dict'):
                params['original_isv_name'] = self.original_isv_name.to_alipay_dict()
            else:
                params['original_isv_name'] = self.original_isv_name
        if self.original_isv_pid:
            if hasattr(self.original_isv_pid, 'to_alipay_dict'):
                params['original_isv_pid'] = self.original_isv_pid.to_alipay_dict()
            else:
                params['original_isv_pid'] = self.original_isv_pid
        if self.out_parking_id:
            if hasattr(self.out_parking_id, 'to_alipay_dict'):
                params['out_parking_id'] = self.out_parking_id.to_alipay_dict()
            else:
                params['out_parking_id'] = self.out_parking_id
        if self.parking_address:
            if hasattr(self.parking_address, 'to_alipay_dict'):
                params['parking_address'] = self.parking_address.to_alipay_dict()
            else:
                params['parking_address'] = self.parking_address
        if self.parking_end_time:
            if hasattr(self.parking_end_time, 'to_alipay_dict'):
                params['parking_end_time'] = self.parking_end_time.to_alipay_dict()
            else:
                params['parking_end_time'] = self.parking_end_time
        if self.parking_fee_description:
            if hasattr(self.parking_fee_description, 'to_alipay_dict'):
                params['parking_fee_description'] = self.parking_fee_description.to_alipay_dict()
            else:
                params['parking_fee_description'] = self.parking_fee_description
        if self.parking_fee_description_img:
            if hasattr(self.parking_fee_description_img, 'to_alipay_dict'):
                params['parking_fee_description_img'] = self.parking_fee_description_img.to_alipay_dict()
            else:
                params['parking_fee_description_img'] = self.parking_fee_description_img
        if self.parking_lot_type:
            if hasattr(self.parking_lot_type, 'to_alipay_dict'):
                params['parking_lot_type'] = self.parking_lot_type.to_alipay_dict()
            else:
                params['parking_lot_type'] = self.parking_lot_type
        if self.parking_mobile:
            if hasattr(self.parking_mobile, 'to_alipay_dict'):
                params['parking_mobile'] = self.parking_mobile.to_alipay_dict()
            else:
                params['parking_mobile'] = self.parking_mobile
        if self.parking_name:
            if hasattr(self.parking_name, 'to_alipay_dict'):
                params['parking_name'] = self.parking_name.to_alipay_dict()
            else:
                params['parking_name'] = self.parking_name
        if self.parking_number:
            if hasattr(self.parking_number, 'to_alipay_dict'):
                params['parking_number'] = self.parking_number.to_alipay_dict()
            else:
                params['parking_number'] = self.parking_number
        if self.parking_poiid:
            if hasattr(self.parking_poiid, 'to_alipay_dict'):
                params['parking_poiid'] = self.parking_poiid.to_alipay_dict()
            else:
                params['parking_poiid'] = self.parking_poiid
        if self.parking_start_time:
            if hasattr(self.parking_start_time, 'to_alipay_dict'):
                params['parking_start_time'] = self.parking_start_time.to_alipay_dict()
            else:
                params['parking_start_time'] = self.parking_start_time
        if self.parking_type:
            if hasattr(self.parking_type, 'to_alipay_dict'):
                params['parking_type'] = self.parking_type.to_alipay_dict()
            else:
                params['parking_type'] = self.parking_type
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.payment_mode:
            if hasattr(self.payment_mode, 'to_alipay_dict'):
                params['payment_mode'] = self.payment_mode.to_alipay_dict()
            else:
                params['payment_mode'] = self.payment_mode
        if self.shopingmall_id:
            if hasattr(self.shopingmall_id, 'to_alipay_dict'):
                params['shopingmall_id'] = self.shopingmall_id.to_alipay_dict()
            else:
                params['shopingmall_id'] = self.shopingmall_id
        if self.sum_space:
            if hasattr(self.sum_space, 'to_alipay_dict'):
                params['sum_space'] = self.sum_space.to_alipay_dict()
            else:
                params['sum_space'] = self.sum_space
        if self.support_after_pay:
            if hasattr(self.support_after_pay, 'to_alipay_dict'):
                params['support_after_pay'] = self.support_after_pay.to_alipay_dict()
            else:
                params['support_after_pay'] = self.support_after_pay
        if self.time_out:
            if hasattr(self.time_out, 'to_alipay_dict'):
                params['time_out'] = self.time_out.to_alipay_dict()
            else:
                params['time_out'] = self.time_out
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingParkinglotinfoCreateModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'business_isv' in d:
            o.business_isv = d['business_isv']
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'contact_alipay' in d:
            o.contact_alipay = d['contact_alipay']
        if 'contact_emali' in d:
            o.contact_emali = d['contact_emali']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_tel' in d:
            o.contact_tel = d['contact_tel']
        if 'contact_weixin' in d:
            o.contact_weixin = d['contact_weixin']
        if 'equipment_name' in d:
            o.equipment_name = d['equipment_name']
        if 'is_support_invoice' in d:
            o.is_support_invoice = d['is_support_invoice']
        if 'isv_mobile' in d:
            o.isv_mobile = d['isv_mobile']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mchnt_id' in d:
            o.mchnt_id = d['mchnt_id']
        if 'original_isv_appid' in d:
            o.original_isv_appid = d['original_isv_appid']
        if 'original_isv_mobile' in d:
            o.original_isv_mobile = d['original_isv_mobile']
        if 'original_isv_name' in d:
            o.original_isv_name = d['original_isv_name']
        if 'original_isv_pid' in d:
            o.original_isv_pid = d['original_isv_pid']
        if 'out_parking_id' in d:
            o.out_parking_id = d['out_parking_id']
        if 'parking_address' in d:
            o.parking_address = d['parking_address']
        if 'parking_end_time' in d:
            o.parking_end_time = d['parking_end_time']
        if 'parking_fee_description' in d:
            o.parking_fee_description = d['parking_fee_description']
        if 'parking_fee_description_img' in d:
            o.parking_fee_description_img = d['parking_fee_description_img']
        if 'parking_lot_type' in d:
            o.parking_lot_type = d['parking_lot_type']
        if 'parking_mobile' in d:
            o.parking_mobile = d['parking_mobile']
        if 'parking_name' in d:
            o.parking_name = d['parking_name']
        if 'parking_number' in d:
            o.parking_number = d['parking_number']
        if 'parking_poiid' in d:
            o.parking_poiid = d['parking_poiid']
        if 'parking_start_time' in d:
            o.parking_start_time = d['parking_start_time']
        if 'parking_type' in d:
            o.parking_type = d['parking_type']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'payment_mode' in d:
            o.payment_mode = d['payment_mode']
        if 'shopingmall_id' in d:
            o.shopingmall_id = d['shopingmall_id']
        if 'sum_space' in d:
            o.sum_space = d['sum_space']
        if 'support_after_pay' in d:
            o.support_after_pay = d['support_after_pay']
        if 'time_out' in d:
            o.time_out = d['time_out']
        return o


