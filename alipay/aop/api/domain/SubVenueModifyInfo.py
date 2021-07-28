#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubVenueModifyInfo(object):

    def __init__(self):
        self._admission_requirement = None
        self._announcement = None
        self._bookable = None
        self._desc = None
        self._equipment_rental = None
        self._facility_list = None
        self._name = None
        self._opening_hours = None
        self._opt_type = None
        self._out_sub_venue_id = None
        self._payee_account = None
        self._payment_method = None
        self._payment_type = None
        self._phone = None
        self._picture_list = None
        self._poster = None
        self._product_type_list = None
        self._promotion = None
        self._status = None
        self._sub_venue_id = None
        self._sub_venue_pid = None
        self._sub_venue_smid = None
        self._tag_list = None
        self._training = None
        self._venue_type = None
        self._vip = None

    @property
    def admission_requirement(self):
        return self._admission_requirement

    @admission_requirement.setter
    def admission_requirement(self, value):
        self._admission_requirement = value
    @property
    def announcement(self):
        return self._announcement

    @announcement.setter
    def announcement(self, value):
        self._announcement = value
    @property
    def bookable(self):
        return self._bookable

    @bookable.setter
    def bookable(self, value):
        self._bookable = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def equipment_rental(self):
        return self._equipment_rental

    @equipment_rental.setter
    def equipment_rental(self, value):
        self._equipment_rental = value
    @property
    def facility_list(self):
        return self._facility_list

    @facility_list.setter
    def facility_list(self, value):
        if isinstance(value, list):
            self._facility_list = list()
            for i in value:
                self._facility_list.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, value):
        self._opening_hours = value
    @property
    def opt_type(self):
        return self._opt_type

    @opt_type.setter
    def opt_type(self, value):
        self._opt_type = value
    @property
    def out_sub_venue_id(self):
        return self._out_sub_venue_id

    @out_sub_venue_id.setter
    def out_sub_venue_id(self, value):
        self._out_sub_venue_id = value
    @property
    def payee_account(self):
        return self._payee_account

    @payee_account.setter
    def payee_account(self, value):
        self._payee_account = value
    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if isinstance(value, list):
            self._phone = list()
            for i in value:
                self._phone.append(i)
    @property
    def picture_list(self):
        return self._picture_list

    @picture_list.setter
    def picture_list(self, value):
        if isinstance(value, list):
            self._picture_list = list()
            for i in value:
                self._picture_list.append(i)
    @property
    def poster(self):
        return self._poster

    @poster.setter
    def poster(self, value):
        self._poster = value
    @property
    def product_type_list(self):
        return self._product_type_list

    @product_type_list.setter
    def product_type_list(self, value):
        if isinstance(value, list):
            self._product_type_list = list()
            for i in value:
                self._product_type_list.append(i)
    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        self._promotion = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_venue_id(self):
        return self._sub_venue_id

    @sub_venue_id.setter
    def sub_venue_id(self, value):
        self._sub_venue_id = value
    @property
    def sub_venue_pid(self):
        return self._sub_venue_pid

    @sub_venue_pid.setter
    def sub_venue_pid(self, value):
        self._sub_venue_pid = value
    @property
    def sub_venue_smid(self):
        return self._sub_venue_smid

    @sub_venue_smid.setter
    def sub_venue_smid(self, value):
        self._sub_venue_smid = value
    @property
    def tag_list(self):
        return self._tag_list

    @tag_list.setter
    def tag_list(self, value):
        if isinstance(value, list):
            self._tag_list = list()
            for i in value:
                self._tag_list.append(i)
    @property
    def training(self):
        return self._training

    @training.setter
    def training(self, value):
        self._training = value
    @property
    def venue_type(self):
        return self._venue_type

    @venue_type.setter
    def venue_type(self, value):
        self._venue_type = value
    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, value):
        self._vip = value


    def to_alipay_dict(self):
        params = dict()
        if self.admission_requirement:
            if hasattr(self.admission_requirement, 'to_alipay_dict'):
                params['admission_requirement'] = self.admission_requirement.to_alipay_dict()
            else:
                params['admission_requirement'] = self.admission_requirement
        if self.announcement:
            if hasattr(self.announcement, 'to_alipay_dict'):
                params['announcement'] = self.announcement.to_alipay_dict()
            else:
                params['announcement'] = self.announcement
        if self.bookable:
            if hasattr(self.bookable, 'to_alipay_dict'):
                params['bookable'] = self.bookable.to_alipay_dict()
            else:
                params['bookable'] = self.bookable
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.equipment_rental:
            if hasattr(self.equipment_rental, 'to_alipay_dict'):
                params['equipment_rental'] = self.equipment_rental.to_alipay_dict()
            else:
                params['equipment_rental'] = self.equipment_rental
        if self.facility_list:
            if isinstance(self.facility_list, list):
                for i in range(0, len(self.facility_list)):
                    element = self.facility_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.facility_list[i] = element.to_alipay_dict()
            if hasattr(self.facility_list, 'to_alipay_dict'):
                params['facility_list'] = self.facility_list.to_alipay_dict()
            else:
                params['facility_list'] = self.facility_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.opening_hours:
            if hasattr(self.opening_hours, 'to_alipay_dict'):
                params['opening_hours'] = self.opening_hours.to_alipay_dict()
            else:
                params['opening_hours'] = self.opening_hours
        if self.opt_type:
            if hasattr(self.opt_type, 'to_alipay_dict'):
                params['opt_type'] = self.opt_type.to_alipay_dict()
            else:
                params['opt_type'] = self.opt_type
        if self.out_sub_venue_id:
            if hasattr(self.out_sub_venue_id, 'to_alipay_dict'):
                params['out_sub_venue_id'] = self.out_sub_venue_id.to_alipay_dict()
            else:
                params['out_sub_venue_id'] = self.out_sub_venue_id
        if self.payee_account:
            if hasattr(self.payee_account, 'to_alipay_dict'):
                params['payee_account'] = self.payee_account.to_alipay_dict()
            else:
                params['payee_account'] = self.payee_account
        if self.payment_method:
            if hasattr(self.payment_method, 'to_alipay_dict'):
                params['payment_method'] = self.payment_method.to_alipay_dict()
            else:
                params['payment_method'] = self.payment_method
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.phone:
            if isinstance(self.phone, list):
                for i in range(0, len(self.phone)):
                    element = self.phone[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone[i] = element.to_alipay_dict()
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.picture_list:
            if isinstance(self.picture_list, list):
                for i in range(0, len(self.picture_list)):
                    element = self.picture_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.picture_list[i] = element.to_alipay_dict()
            if hasattr(self.picture_list, 'to_alipay_dict'):
                params['picture_list'] = self.picture_list.to_alipay_dict()
            else:
                params['picture_list'] = self.picture_list
        if self.poster:
            if hasattr(self.poster, 'to_alipay_dict'):
                params['poster'] = self.poster.to_alipay_dict()
            else:
                params['poster'] = self.poster
        if self.product_type_list:
            if isinstance(self.product_type_list, list):
                for i in range(0, len(self.product_type_list)):
                    element = self.product_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_type_list[i] = element.to_alipay_dict()
            if hasattr(self.product_type_list, 'to_alipay_dict'):
                params['product_type_list'] = self.product_type_list.to_alipay_dict()
            else:
                params['product_type_list'] = self.product_type_list
        if self.promotion:
            if hasattr(self.promotion, 'to_alipay_dict'):
                params['promotion'] = self.promotion.to_alipay_dict()
            else:
                params['promotion'] = self.promotion
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_venue_id:
            if hasattr(self.sub_venue_id, 'to_alipay_dict'):
                params['sub_venue_id'] = self.sub_venue_id.to_alipay_dict()
            else:
                params['sub_venue_id'] = self.sub_venue_id
        if self.sub_venue_pid:
            if hasattr(self.sub_venue_pid, 'to_alipay_dict'):
                params['sub_venue_pid'] = self.sub_venue_pid.to_alipay_dict()
            else:
                params['sub_venue_pid'] = self.sub_venue_pid
        if self.sub_venue_smid:
            if hasattr(self.sub_venue_smid, 'to_alipay_dict'):
                params['sub_venue_smid'] = self.sub_venue_smid.to_alipay_dict()
            else:
                params['sub_venue_smid'] = self.sub_venue_smid
        if self.tag_list:
            if isinstance(self.tag_list, list):
                for i in range(0, len(self.tag_list)):
                    element = self.tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_list[i] = element.to_alipay_dict()
            if hasattr(self.tag_list, 'to_alipay_dict'):
                params['tag_list'] = self.tag_list.to_alipay_dict()
            else:
                params['tag_list'] = self.tag_list
        if self.training:
            if hasattr(self.training, 'to_alipay_dict'):
                params['training'] = self.training.to_alipay_dict()
            else:
                params['training'] = self.training
        if self.venue_type:
            if hasattr(self.venue_type, 'to_alipay_dict'):
                params['venue_type'] = self.venue_type.to_alipay_dict()
            else:
                params['venue_type'] = self.venue_type
        if self.vip:
            if hasattr(self.vip, 'to_alipay_dict'):
                params['vip'] = self.vip.to_alipay_dict()
            else:
                params['vip'] = self.vip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubVenueModifyInfo()
        if 'admission_requirement' in d:
            o.admission_requirement = d['admission_requirement']
        if 'announcement' in d:
            o.announcement = d['announcement']
        if 'bookable' in d:
            o.bookable = d['bookable']
        if 'desc' in d:
            o.desc = d['desc']
        if 'equipment_rental' in d:
            o.equipment_rental = d['equipment_rental']
        if 'facility_list' in d:
            o.facility_list = d['facility_list']
        if 'name' in d:
            o.name = d['name']
        if 'opening_hours' in d:
            o.opening_hours = d['opening_hours']
        if 'opt_type' in d:
            o.opt_type = d['opt_type']
        if 'out_sub_venue_id' in d:
            o.out_sub_venue_id = d['out_sub_venue_id']
        if 'payee_account' in d:
            o.payee_account = d['payee_account']
        if 'payment_method' in d:
            o.payment_method = d['payment_method']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'picture_list' in d:
            o.picture_list = d['picture_list']
        if 'poster' in d:
            o.poster = d['poster']
        if 'product_type_list' in d:
            o.product_type_list = d['product_type_list']
        if 'promotion' in d:
            o.promotion = d['promotion']
        if 'status' in d:
            o.status = d['status']
        if 'sub_venue_id' in d:
            o.sub_venue_id = d['sub_venue_id']
        if 'sub_venue_pid' in d:
            o.sub_venue_pid = d['sub_venue_pid']
        if 'sub_venue_smid' in d:
            o.sub_venue_smid = d['sub_venue_smid']
        if 'tag_list' in d:
            o.tag_list = d['tag_list']
        if 'training' in d:
            o.training = d['training']
        if 'venue_type' in d:
            o.venue_type = d['venue_type']
        if 'vip' in d:
            o.vip = d['vip']
        return o


