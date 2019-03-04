#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OcrIdentifyResult(object):

    def __init__(self):
        self._addr = None
        self._address = None
        self._birth = None
        self._business = None
        self._captial = None
        self._card_num = None
        self._code = None
        self._end_date = None
        self._engine_num = None
        self._establish_date = None
        self._issue_date = None
        self._msg = None
        self._name = None
        self._nationality = None
        self._num = None
        self._owner = None
        self._person = None
        self._plate_num = None
        self._reg_num = None
        self._register_date = None
        self._request_id = None
        self._sex = None
        self._start_date = None
        self._success = None
        self._trace_id = None
        self._use_character = None
        self._valid_period = None
        self._vehicle_type = None
        self._vin = None

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, value):
        self._addr = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value
    @property
    def captial(self):
        return self._captial

    @captial.setter
    def captial(self, value):
        self._captial = value
    @property
    def card_num(self):
        return self._card_num

    @card_num.setter
    def card_num(self, value):
        self._card_num = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def engine_num(self):
        return self._engine_num

    @engine_num.setter
    def engine_num(self, value):
        self._engine_num = value
    @property
    def establish_date(self):
        return self._establish_date

    @establish_date.setter
    def establish_date(self, value):
        self._establish_date = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        self._person = value
    @property
    def plate_num(self):
        return self._plate_num

    @plate_num.setter
    def plate_num(self, value):
        self._plate_num = value
    @property
    def reg_num(self):
        return self._reg_num

    @reg_num.setter
    def reg_num(self, value):
        self._reg_num = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def use_character(self):
        return self._use_character

    @use_character.setter
    def use_character(self, value):
        self._use_character = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        self._valid_period = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.addr:
            if hasattr(self.addr, 'to_alipay_dict'):
                params['addr'] = self.addr.to_alipay_dict()
            else:
                params['addr'] = self.addr
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.birth:
            if hasattr(self.birth, 'to_alipay_dict'):
                params['birth'] = self.birth.to_alipay_dict()
            else:
                params['birth'] = self.birth
        if self.business:
            if hasattr(self.business, 'to_alipay_dict'):
                params['business'] = self.business.to_alipay_dict()
            else:
                params['business'] = self.business
        if self.captial:
            if hasattr(self.captial, 'to_alipay_dict'):
                params['captial'] = self.captial.to_alipay_dict()
            else:
                params['captial'] = self.captial
        if self.card_num:
            if hasattr(self.card_num, 'to_alipay_dict'):
                params['card_num'] = self.card_num.to_alipay_dict()
            else:
                params['card_num'] = self.card_num
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.engine_num:
            if hasattr(self.engine_num, 'to_alipay_dict'):
                params['engine_num'] = self.engine_num.to_alipay_dict()
            else:
                params['engine_num'] = self.engine_num
        if self.establish_date:
            if hasattr(self.establish_date, 'to_alipay_dict'):
                params['establish_date'] = self.establish_date.to_alipay_dict()
            else:
                params['establish_date'] = self.establish_date
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.person:
            if hasattr(self.person, 'to_alipay_dict'):
                params['person'] = self.person.to_alipay_dict()
            else:
                params['person'] = self.person
        if self.plate_num:
            if hasattr(self.plate_num, 'to_alipay_dict'):
                params['plate_num'] = self.plate_num.to_alipay_dict()
            else:
                params['plate_num'] = self.plate_num
        if self.reg_num:
            if hasattr(self.reg_num, 'to_alipay_dict'):
                params['reg_num'] = self.reg_num.to_alipay_dict()
            else:
                params['reg_num'] = self.reg_num
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.use_character:
            if hasattr(self.use_character, 'to_alipay_dict'):
                params['use_character'] = self.use_character.to_alipay_dict()
            else:
                params['use_character'] = self.use_character
        if self.valid_period:
            if hasattr(self.valid_period, 'to_alipay_dict'):
                params['valid_period'] = self.valid_period.to_alipay_dict()
            else:
                params['valid_period'] = self.valid_period
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OcrIdentifyResult()
        if 'addr' in d:
            o.addr = d['addr']
        if 'address' in d:
            o.address = d['address']
        if 'birth' in d:
            o.birth = d['birth']
        if 'business' in d:
            o.business = d['business']
        if 'captial' in d:
            o.captial = d['captial']
        if 'card_num' in d:
            o.card_num = d['card_num']
        if 'code' in d:
            o.code = d['code']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'engine_num' in d:
            o.engine_num = d['engine_num']
        if 'establish_date' in d:
            o.establish_date = d['establish_date']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'msg' in d:
            o.msg = d['msg']
        if 'name' in d:
            o.name = d['name']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'num' in d:
            o.num = d['num']
        if 'owner' in d:
            o.owner = d['owner']
        if 'person' in d:
            o.person = d['person']
        if 'plate_num' in d:
            o.plate_num = d['plate_num']
        if 'reg_num' in d:
            o.reg_num = d['reg_num']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sex' in d:
            o.sex = d['sex']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'success' in d:
            o.success = d['success']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'use_character' in d:
            o.use_character = d['use_character']
        if 'valid_period' in d:
            o.valid_period = d['valid_period']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vin' in d:
            o.vin = d['vin']
        return o


