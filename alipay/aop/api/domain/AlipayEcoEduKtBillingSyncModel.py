#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduPayItems import EduPayItems
from alipay.aop.api.domain.BillSyncExtInfo import BillSyncExtInfo
from alipay.aop.api.domain.UserDetails import UserDetails


class AlipayEcoEduKtBillingSyncModel(object):

    def __init__(self):
        self._campus_id = None
        self._campus_name = None
        self._charge_items = None
        self._city = None
        self._current_class = None
        self._current_grade = None
        self._district = None
        self._district_code = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modify = None
        self._gmt_paytime = None
        self._isv_order_no = None
        self._order_amount = None
        self._order_status = None
        self._pay_amount = None
        self._pay_user_id = None
        self._province = None
        self._school_code = None
        self._school_external_id = None
        self._school_name = None
        self._school_pid = None
        self._school_property = None
        self._school_type = None
        self._source = None
        self._student_code = None
        self._student_name = None
        self._sub_orgname = None
        self._sub_orgtype = None
        self._sys_service_param = None
        self._sys_service_provider_id = None
        self._title = None
        self._trade_no = None
        self._trans_currency = None
        self._user = None

    @property
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def charge_items(self):
        return self._charge_items

    @charge_items.setter
    def charge_items(self, value):
        if isinstance(value, list):
            self._charge_items = list()
            for i in value:
                if isinstance(i, EduPayItems):
                    self._charge_items.append(i)
                else:
                    self._charge_items.append(EduPayItems.from_alipay_dict(i))
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def current_class(self):
        return self._current_class

    @current_class.setter
    def current_class(self, value):
        self._current_class = value
    @property
    def current_grade(self):
        return self._current_grade

    @current_grade.setter
    def current_grade(self, value):
        self._current_grade = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, BillSyncExtInfo):
            self._ext_info = value
        else:
            self._ext_info = BillSyncExtInfo.from_alipay_dict(value)
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modify(self):
        return self._gmt_modify

    @gmt_modify.setter
    def gmt_modify(self, value):
        self._gmt_modify = value
    @property
    def gmt_paytime(self):
        return self._gmt_paytime

    @gmt_paytime.setter
    def gmt_paytime(self, value):
        self._gmt_paytime = value
    @property
    def isv_order_no(self):
        return self._isv_order_no

    @isv_order_no.setter
    def isv_order_no(self, value):
        self._isv_order_no = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_user_id(self):
        return self._pay_user_id

    @pay_user_id.setter
    def pay_user_id(self, value):
        self._pay_user_id = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def school_code(self):
        return self._school_code

    @school_code.setter
    def school_code(self, value):
        self._school_code = value
    @property
    def school_external_id(self):
        return self._school_external_id

    @school_external_id.setter
    def school_external_id(self, value):
        self._school_external_id = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def school_property(self):
        return self._school_property

    @school_property.setter
    def school_property(self, value):
        self._school_property = value
    @property
    def school_type(self):
        return self._school_type

    @school_type.setter
    def school_type(self, value):
        self._school_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def student_code(self):
        return self._student_code

    @student_code.setter
    def student_code(self, value):
        self._student_code = value
    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        self._student_name = value
    @property
    def sub_orgname(self):
        return self._sub_orgname

    @sub_orgname.setter
    def sub_orgname(self, value):
        self._sub_orgname = value
    @property
    def sub_orgtype(self):
        return self._sub_orgtype

    @sub_orgtype.setter
    def sub_orgtype(self, value):
        self._sub_orgtype = value
    @property
    def sys_service_param(self):
        return self._sys_service_param

    @sys_service_param.setter
    def sys_service_param(self, value):
        self._sys_service_param = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserDetails):
            self._user = value
        else:
            self._user = UserDetails.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.charge_items:
            if isinstance(self.charge_items, list):
                for i in range(0, len(self.charge_items)):
                    element = self.charge_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.charge_items[i] = element.to_alipay_dict()
            if hasattr(self.charge_items, 'to_alipay_dict'):
                params['charge_items'] = self.charge_items.to_alipay_dict()
            else:
                params['charge_items'] = self.charge_items
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.current_class:
            if hasattr(self.current_class, 'to_alipay_dict'):
                params['current_class'] = self.current_class.to_alipay_dict()
            else:
                params['current_class'] = self.current_class
        if self.current_grade:
            if hasattr(self.current_grade, 'to_alipay_dict'):
                params['current_grade'] = self.current_grade.to_alipay_dict()
            else:
                params['current_grade'] = self.current_grade
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modify:
            if hasattr(self.gmt_modify, 'to_alipay_dict'):
                params['gmt_modify'] = self.gmt_modify.to_alipay_dict()
            else:
                params['gmt_modify'] = self.gmt_modify
        if self.gmt_paytime:
            if hasattr(self.gmt_paytime, 'to_alipay_dict'):
                params['gmt_paytime'] = self.gmt_paytime.to_alipay_dict()
            else:
                params['gmt_paytime'] = self.gmt_paytime
        if self.isv_order_no:
            if hasattr(self.isv_order_no, 'to_alipay_dict'):
                params['isv_order_no'] = self.isv_order_no.to_alipay_dict()
            else:
                params['isv_order_no'] = self.isv_order_no
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_user_id:
            if hasattr(self.pay_user_id, 'to_alipay_dict'):
                params['pay_user_id'] = self.pay_user_id.to_alipay_dict()
            else:
                params['pay_user_id'] = self.pay_user_id
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.school_code:
            if hasattr(self.school_code, 'to_alipay_dict'):
                params['school_code'] = self.school_code.to_alipay_dict()
            else:
                params['school_code'] = self.school_code
        if self.school_external_id:
            if hasattr(self.school_external_id, 'to_alipay_dict'):
                params['school_external_id'] = self.school_external_id.to_alipay_dict()
            else:
                params['school_external_id'] = self.school_external_id
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.school_property:
            if hasattr(self.school_property, 'to_alipay_dict'):
                params['school_property'] = self.school_property.to_alipay_dict()
            else:
                params['school_property'] = self.school_property
        if self.school_type:
            if hasattr(self.school_type, 'to_alipay_dict'):
                params['school_type'] = self.school_type.to_alipay_dict()
            else:
                params['school_type'] = self.school_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.student_code:
            if hasattr(self.student_code, 'to_alipay_dict'):
                params['student_code'] = self.student_code.to_alipay_dict()
            else:
                params['student_code'] = self.student_code
        if self.student_name:
            if hasattr(self.student_name, 'to_alipay_dict'):
                params['student_name'] = self.student_name.to_alipay_dict()
            else:
                params['student_name'] = self.student_name
        if self.sub_orgname:
            if hasattr(self.sub_orgname, 'to_alipay_dict'):
                params['sub_orgname'] = self.sub_orgname.to_alipay_dict()
            else:
                params['sub_orgname'] = self.sub_orgname
        if self.sub_orgtype:
            if hasattr(self.sub_orgtype, 'to_alipay_dict'):
                params['sub_orgtype'] = self.sub_orgtype.to_alipay_dict()
            else:
                params['sub_orgtype'] = self.sub_orgtype
        if self.sys_service_param:
            if hasattr(self.sys_service_param, 'to_alipay_dict'):
                params['sys_service_param'] = self.sys_service_param.to_alipay_dict()
            else:
                params['sys_service_param'] = self.sys_service_param
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtBillingSyncModel()
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'charge_items' in d:
            o.charge_items = d['charge_items']
        if 'city' in d:
            o.city = d['city']
        if 'current_class' in d:
            o.current_class = d['current_class']
        if 'current_grade' in d:
            o.current_grade = d['current_grade']
        if 'district' in d:
            o.district = d['district']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modify' in d:
            o.gmt_modify = d['gmt_modify']
        if 'gmt_paytime' in d:
            o.gmt_paytime = d['gmt_paytime']
        if 'isv_order_no' in d:
            o.isv_order_no = d['isv_order_no']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_user_id' in d:
            o.pay_user_id = d['pay_user_id']
        if 'province' in d:
            o.province = d['province']
        if 'school_code' in d:
            o.school_code = d['school_code']
        if 'school_external_id' in d:
            o.school_external_id = d['school_external_id']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'school_property' in d:
            o.school_property = d['school_property']
        if 'school_type' in d:
            o.school_type = d['school_type']
        if 'source' in d:
            o.source = d['source']
        if 'student_code' in d:
            o.student_code = d['student_code']
        if 'student_name' in d:
            o.student_name = d['student_name']
        if 'sub_orgname' in d:
            o.sub_orgname = d['sub_orgname']
        if 'sub_orgtype' in d:
            o.sub_orgtype = d['sub_orgtype']
        if 'sys_service_param' in d:
            o.sys_service_param = d['sys_service_param']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        if 'title' in d:
            o.title = d['title']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        if 'user' in d:
            o.user = d['user']
        return o


