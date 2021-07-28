#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcEcodataSyncModel(object):

    def __init__(self):
        self._acquire_inst = None
        self._agent_flag = None
        self._agree_id = None
        self._apply_type = None
        self._approved_load = None
        self._axle_count = None
        self._biz_agreement_no = None
        self._biz_time = None
        self._brand_model = None
        self._card_no = None
        self._device_no = None
        self._engine_no = None
        self._etc_name = None
        self._grant_date = None
        self._gross_mass = None
        self._order_status = None
        self._out_biz_no = None
        self._outline_size = None
        self._plate_color = None
        self._plate_no = None
        self._register_date = None
        self._seller_id = None
        self._seller_name = None
        self._traction_mass = None
        self._unladen_mass = None
        self._user_id = None
        self._user_mobile = None
        self._vehicle_ac = None
        self._vehicle_owner_name = None
        self._vehicle_type = None
        self._vehicle_use_type = None
        self._vin = None

    @property
    def acquire_inst(self):
        return self._acquire_inst

    @acquire_inst.setter
    def acquire_inst(self, value):
        self._acquire_inst = value
    @property
    def agent_flag(self):
        return self._agent_flag

    @agent_flag.setter
    def agent_flag(self, value):
        self._agent_flag = value
    @property
    def agree_id(self):
        return self._agree_id

    @agree_id.setter
    def agree_id(self, value):
        self._agree_id = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def approved_load(self):
        return self._approved_load

    @approved_load.setter
    def approved_load(self, value):
        self._approved_load = value
    @property
    def axle_count(self):
        return self._axle_count

    @axle_count.setter
    def axle_count(self, value):
        self._axle_count = value
    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def brand_model(self):
        return self._brand_model

    @brand_model.setter
    def brand_model(self, value):
        self._brand_model = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def device_no(self):
        return self._device_no

    @device_no.setter
    def device_no(self, value):
        self._device_no = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def etc_name(self):
        return self._etc_name

    @etc_name.setter
    def etc_name(self, value):
        self._etc_name = value
    @property
    def grant_date(self):
        return self._grant_date

    @grant_date.setter
    def grant_date(self, value):
        self._grant_date = value
    @property
    def gross_mass(self):
        return self._gross_mass

    @gross_mass.setter
    def gross_mass(self, value):
        self._gross_mass = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def outline_size(self):
        return self._outline_size

    @outline_size.setter
    def outline_size(self, value):
        self._outline_size = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_name(self):
        return self._seller_name

    @seller_name.setter
    def seller_name(self, value):
        self._seller_name = value
    @property
    def traction_mass(self):
        return self._traction_mass

    @traction_mass.setter
    def traction_mass(self, value):
        self._traction_mass = value
    @property
    def unladen_mass(self):
        return self._unladen_mass

    @unladen_mass.setter
    def unladen_mass(self, value):
        self._unladen_mass = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value
    @property
    def vehicle_ac(self):
        return self._vehicle_ac

    @vehicle_ac.setter
    def vehicle_ac(self, value):
        self._vehicle_ac = value
    @property
    def vehicle_owner_name(self):
        return self._vehicle_owner_name

    @vehicle_owner_name.setter
    def vehicle_owner_name(self, value):
        self._vehicle_owner_name = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vehicle_use_type(self):
        return self._vehicle_use_type

    @vehicle_use_type.setter
    def vehicle_use_type(self, value):
        self._vehicle_use_type = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_inst:
            if hasattr(self.acquire_inst, 'to_alipay_dict'):
                params['acquire_inst'] = self.acquire_inst.to_alipay_dict()
            else:
                params['acquire_inst'] = self.acquire_inst
        if self.agent_flag:
            if hasattr(self.agent_flag, 'to_alipay_dict'):
                params['agent_flag'] = self.agent_flag.to_alipay_dict()
            else:
                params['agent_flag'] = self.agent_flag
        if self.agree_id:
            if hasattr(self.agree_id, 'to_alipay_dict'):
                params['agree_id'] = self.agree_id.to_alipay_dict()
            else:
                params['agree_id'] = self.agree_id
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.approved_load:
            if hasattr(self.approved_load, 'to_alipay_dict'):
                params['approved_load'] = self.approved_load.to_alipay_dict()
            else:
                params['approved_load'] = self.approved_load
        if self.axle_count:
            if hasattr(self.axle_count, 'to_alipay_dict'):
                params['axle_count'] = self.axle_count.to_alipay_dict()
            else:
                params['axle_count'] = self.axle_count
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.brand_model:
            if hasattr(self.brand_model, 'to_alipay_dict'):
                params['brand_model'] = self.brand_model.to_alipay_dict()
            else:
                params['brand_model'] = self.brand_model
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.device_no:
            if hasattr(self.device_no, 'to_alipay_dict'):
                params['device_no'] = self.device_no.to_alipay_dict()
            else:
                params['device_no'] = self.device_no
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.etc_name:
            if hasattr(self.etc_name, 'to_alipay_dict'):
                params['etc_name'] = self.etc_name.to_alipay_dict()
            else:
                params['etc_name'] = self.etc_name
        if self.grant_date:
            if hasattr(self.grant_date, 'to_alipay_dict'):
                params['grant_date'] = self.grant_date.to_alipay_dict()
            else:
                params['grant_date'] = self.grant_date
        if self.gross_mass:
            if hasattr(self.gross_mass, 'to_alipay_dict'):
                params['gross_mass'] = self.gross_mass.to_alipay_dict()
            else:
                params['gross_mass'] = self.gross_mass
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.outline_size:
            if hasattr(self.outline_size, 'to_alipay_dict'):
                params['outline_size'] = self.outline_size.to_alipay_dict()
            else:
                params['outline_size'] = self.outline_size
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_name:
            if hasattr(self.seller_name, 'to_alipay_dict'):
                params['seller_name'] = self.seller_name.to_alipay_dict()
            else:
                params['seller_name'] = self.seller_name
        if self.traction_mass:
            if hasattr(self.traction_mass, 'to_alipay_dict'):
                params['traction_mass'] = self.traction_mass.to_alipay_dict()
            else:
                params['traction_mass'] = self.traction_mass
        if self.unladen_mass:
            if hasattr(self.unladen_mass, 'to_alipay_dict'):
                params['unladen_mass'] = self.unladen_mass.to_alipay_dict()
            else:
                params['unladen_mass'] = self.unladen_mass
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
        if self.vehicle_ac:
            if hasattr(self.vehicle_ac, 'to_alipay_dict'):
                params['vehicle_ac'] = self.vehicle_ac.to_alipay_dict()
            else:
                params['vehicle_ac'] = self.vehicle_ac
        if self.vehicle_owner_name:
            if hasattr(self.vehicle_owner_name, 'to_alipay_dict'):
                params['vehicle_owner_name'] = self.vehicle_owner_name.to_alipay_dict()
            else:
                params['vehicle_owner_name'] = self.vehicle_owner_name
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.vehicle_use_type:
            if hasattr(self.vehicle_use_type, 'to_alipay_dict'):
                params['vehicle_use_type'] = self.vehicle_use_type.to_alipay_dict()
            else:
                params['vehicle_use_type'] = self.vehicle_use_type
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
        o = AlipayCommerceTransportEtcEcodataSyncModel()
        if 'acquire_inst' in d:
            o.acquire_inst = d['acquire_inst']
        if 'agent_flag' in d:
            o.agent_flag = d['agent_flag']
        if 'agree_id' in d:
            o.agree_id = d['agree_id']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'approved_load' in d:
            o.approved_load = d['approved_load']
        if 'axle_count' in d:
            o.axle_count = d['axle_count']
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'brand_model' in d:
            o.brand_model = d['brand_model']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'device_no' in d:
            o.device_no = d['device_no']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'etc_name' in d:
            o.etc_name = d['etc_name']
        if 'grant_date' in d:
            o.grant_date = d['grant_date']
        if 'gross_mass' in d:
            o.gross_mass = d['gross_mass']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'outline_size' in d:
            o.outline_size = d['outline_size']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_name' in d:
            o.seller_name = d['seller_name']
        if 'traction_mass' in d:
            o.traction_mass = d['traction_mass']
        if 'unladen_mass' in d:
            o.unladen_mass = d['unladen_mass']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        if 'vehicle_ac' in d:
            o.vehicle_ac = d['vehicle_ac']
        if 'vehicle_owner_name' in d:
            o.vehicle_owner_name = d['vehicle_owner_name']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vehicle_use_type' in d:
            o.vehicle_use_type = d['vehicle_use_type']
        if 'vin' in d:
            o.vin = d['vin']
        return o


