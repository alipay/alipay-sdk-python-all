#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcomItemExtendDetailDTO(object):

    def __init__(self):
        self._card_type = None
        self._card_use_amount = None
        self._card_use_count = None
        self._card_use_period = None
        self._charge_station_address = None
        self._charge_station_area = None
        self._charge_station_city = None
        self._charge_station_no = None
        self._charge_station_plug_total = None
        self._charge_station_prov = None
        self._charge_station_town = None
        self._charge_type = None
        self._ext_info = None
        self._game_account = None
        self._game_account_client = None
        self._game_account_client_id = None
        self._game_id = None
        self._game_name = None
        self._game_trade_mode = None
        self._lockable_device = None
        self._plug_no = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def card_use_amount(self):
        return self._card_use_amount

    @card_use_amount.setter
    def card_use_amount(self, value):
        self._card_use_amount = value
    @property
    def card_use_count(self):
        return self._card_use_count

    @card_use_count.setter
    def card_use_count(self, value):
        self._card_use_count = value
    @property
    def card_use_period(self):
        return self._card_use_period

    @card_use_period.setter
    def card_use_period(self, value):
        self._card_use_period = value
    @property
    def charge_station_address(self):
        return self._charge_station_address

    @charge_station_address.setter
    def charge_station_address(self, value):
        self._charge_station_address = value
    @property
    def charge_station_area(self):
        return self._charge_station_area

    @charge_station_area.setter
    def charge_station_area(self, value):
        self._charge_station_area = value
    @property
    def charge_station_city(self):
        return self._charge_station_city

    @charge_station_city.setter
    def charge_station_city(self, value):
        self._charge_station_city = value
    @property
    def charge_station_no(self):
        return self._charge_station_no

    @charge_station_no.setter
    def charge_station_no(self, value):
        self._charge_station_no = value
    @property
    def charge_station_plug_total(self):
        return self._charge_station_plug_total

    @charge_station_plug_total.setter
    def charge_station_plug_total(self, value):
        self._charge_station_plug_total = value
    @property
    def charge_station_prov(self):
        return self._charge_station_prov

    @charge_station_prov.setter
    def charge_station_prov(self, value):
        self._charge_station_prov = value
    @property
    def charge_station_town(self):
        return self._charge_station_town

    @charge_station_town.setter
    def charge_station_town(self, value):
        self._charge_station_town = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def game_account(self):
        return self._game_account

    @game_account.setter
    def game_account(self, value):
        self._game_account = value
    @property
    def game_account_client(self):
        return self._game_account_client

    @game_account_client.setter
    def game_account_client(self, value):
        self._game_account_client = value
    @property
    def game_account_client_id(self):
        return self._game_account_client_id

    @game_account_client_id.setter
    def game_account_client_id(self, value):
        self._game_account_client_id = value
    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        self._game_id = value
    @property
    def game_name(self):
        return self._game_name

    @game_name.setter
    def game_name(self, value):
        self._game_name = value
    @property
    def game_trade_mode(self):
        return self._game_trade_mode

    @game_trade_mode.setter
    def game_trade_mode(self, value):
        self._game_trade_mode = value
    @property
    def lockable_device(self):
        return self._lockable_device

    @lockable_device.setter
    def lockable_device(self, value):
        self._lockable_device = value
    @property
    def plug_no(self):
        return self._plug_no

    @plug_no.setter
    def plug_no(self, value):
        self._plug_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.card_use_amount:
            if hasattr(self.card_use_amount, 'to_alipay_dict'):
                params['card_use_amount'] = self.card_use_amount.to_alipay_dict()
            else:
                params['card_use_amount'] = self.card_use_amount
        if self.card_use_count:
            if hasattr(self.card_use_count, 'to_alipay_dict'):
                params['card_use_count'] = self.card_use_count.to_alipay_dict()
            else:
                params['card_use_count'] = self.card_use_count
        if self.card_use_period:
            if hasattr(self.card_use_period, 'to_alipay_dict'):
                params['card_use_period'] = self.card_use_period.to_alipay_dict()
            else:
                params['card_use_period'] = self.card_use_period
        if self.charge_station_address:
            if hasattr(self.charge_station_address, 'to_alipay_dict'):
                params['charge_station_address'] = self.charge_station_address.to_alipay_dict()
            else:
                params['charge_station_address'] = self.charge_station_address
        if self.charge_station_area:
            if hasattr(self.charge_station_area, 'to_alipay_dict'):
                params['charge_station_area'] = self.charge_station_area.to_alipay_dict()
            else:
                params['charge_station_area'] = self.charge_station_area
        if self.charge_station_city:
            if hasattr(self.charge_station_city, 'to_alipay_dict'):
                params['charge_station_city'] = self.charge_station_city.to_alipay_dict()
            else:
                params['charge_station_city'] = self.charge_station_city
        if self.charge_station_no:
            if hasattr(self.charge_station_no, 'to_alipay_dict'):
                params['charge_station_no'] = self.charge_station_no.to_alipay_dict()
            else:
                params['charge_station_no'] = self.charge_station_no
        if self.charge_station_plug_total:
            if hasattr(self.charge_station_plug_total, 'to_alipay_dict'):
                params['charge_station_plug_total'] = self.charge_station_plug_total.to_alipay_dict()
            else:
                params['charge_station_plug_total'] = self.charge_station_plug_total
        if self.charge_station_prov:
            if hasattr(self.charge_station_prov, 'to_alipay_dict'):
                params['charge_station_prov'] = self.charge_station_prov.to_alipay_dict()
            else:
                params['charge_station_prov'] = self.charge_station_prov
        if self.charge_station_town:
            if hasattr(self.charge_station_town, 'to_alipay_dict'):
                params['charge_station_town'] = self.charge_station_town.to_alipay_dict()
            else:
                params['charge_station_town'] = self.charge_station_town
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.game_account:
            if hasattr(self.game_account, 'to_alipay_dict'):
                params['game_account'] = self.game_account.to_alipay_dict()
            else:
                params['game_account'] = self.game_account
        if self.game_account_client:
            if hasattr(self.game_account_client, 'to_alipay_dict'):
                params['game_account_client'] = self.game_account_client.to_alipay_dict()
            else:
                params['game_account_client'] = self.game_account_client
        if self.game_account_client_id:
            if hasattr(self.game_account_client_id, 'to_alipay_dict'):
                params['game_account_client_id'] = self.game_account_client_id.to_alipay_dict()
            else:
                params['game_account_client_id'] = self.game_account_client_id
        if self.game_id:
            if hasattr(self.game_id, 'to_alipay_dict'):
                params['game_id'] = self.game_id.to_alipay_dict()
            else:
                params['game_id'] = self.game_id
        if self.game_name:
            if hasattr(self.game_name, 'to_alipay_dict'):
                params['game_name'] = self.game_name.to_alipay_dict()
            else:
                params['game_name'] = self.game_name
        if self.game_trade_mode:
            if hasattr(self.game_trade_mode, 'to_alipay_dict'):
                params['game_trade_mode'] = self.game_trade_mode.to_alipay_dict()
            else:
                params['game_trade_mode'] = self.game_trade_mode
        if self.lockable_device:
            if hasattr(self.lockable_device, 'to_alipay_dict'):
                params['lockable_device'] = self.lockable_device.to_alipay_dict()
            else:
                params['lockable_device'] = self.lockable_device
        if self.plug_no:
            if hasattr(self.plug_no, 'to_alipay_dict'):
                params['plug_no'] = self.plug_no.to_alipay_dict()
            else:
                params['plug_no'] = self.plug_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomItemExtendDetailDTO()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'card_use_amount' in d:
            o.card_use_amount = d['card_use_amount']
        if 'card_use_count' in d:
            o.card_use_count = d['card_use_count']
        if 'card_use_period' in d:
            o.card_use_period = d['card_use_period']
        if 'charge_station_address' in d:
            o.charge_station_address = d['charge_station_address']
        if 'charge_station_area' in d:
            o.charge_station_area = d['charge_station_area']
        if 'charge_station_city' in d:
            o.charge_station_city = d['charge_station_city']
        if 'charge_station_no' in d:
            o.charge_station_no = d['charge_station_no']
        if 'charge_station_plug_total' in d:
            o.charge_station_plug_total = d['charge_station_plug_total']
        if 'charge_station_prov' in d:
            o.charge_station_prov = d['charge_station_prov']
        if 'charge_station_town' in d:
            o.charge_station_town = d['charge_station_town']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'game_account' in d:
            o.game_account = d['game_account']
        if 'game_account_client' in d:
            o.game_account_client = d['game_account_client']
        if 'game_account_client_id' in d:
            o.game_account_client_id = d['game_account_client_id']
        if 'game_id' in d:
            o.game_id = d['game_id']
        if 'game_name' in d:
            o.game_name = d['game_name']
        if 'game_trade_mode' in d:
            o.game_trade_mode = d['game_trade_mode']
        if 'lockable_device' in d:
            o.lockable_device = d['lockable_device']
        if 'plug_no' in d:
            o.plug_no = d['plug_no']
        return o


