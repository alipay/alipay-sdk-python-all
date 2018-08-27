#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipaySecurityRiskDetectRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._buyer_account_no = None
        self._buyer_bind_bankcard = None
        self._buyer_bind_bankcard_type = None
        self._buyer_bind_mobile = None
        self._buyer_grade = None
        self._buyer_identity_no = None
        self._buyer_identity_type = None
        self._buyer_real_name = None
        self._buyer_reg_date = None
        self._buyer_reg_email = None
        self._buyer_reg_mobile = None
        self._buyer_scene_bankcard = None
        self._buyer_scene_bankcard_type = None
        self._buyer_scene_email = None
        self._buyer_scene_mobile = None
        self._currency = None
        self._env_client_base_band = None
        self._env_client_base_station = None
        self._env_client_coordinates = None
        self._env_client_imei = None
        self._env_client_imsi = None
        self._env_client_ios_udid = None
        self._env_client_ip = None
        self._env_client_mac = None
        self._env_client_screen = None
        self._env_client_uuid = None
        self._item_quantity = None
        self._item_unit_price = None
        self._js_token_id = None
        self._order_amount = None
        self._order_category = None
        self._order_credate_time = None
        self._order_item_city = None
        self._order_item_name = None
        self._order_no = None
        self._partner_id = None
        self._receiver_address = None
        self._receiver_city = None
        self._receiver_district = None
        self._receiver_email = None
        self._receiver_mobile = None
        self._receiver_name = None
        self._receiver_state = None
        self._receiver_zip = None
        self._scene_code = None
        self._seller_account_no = None
        self._seller_bind_bankcard = None
        self._seller_bind_bankcard_type = None
        self._seller_bind_mobile = None
        self._seller_identity_no = None
        self._seller_identity_type = None
        self._seller_real_name = None
        self._seller_reg_date = None
        self._seller_reg_email = None
        self._seller_reg_moile = None
        self._transport_type = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def buyer_account_no(self):
        return self._buyer_account_no

    @buyer_account_no.setter
    def buyer_account_no(self, value):
        self._buyer_account_no = value
    @property
    def buyer_bind_bankcard(self):
        return self._buyer_bind_bankcard

    @buyer_bind_bankcard.setter
    def buyer_bind_bankcard(self, value):
        self._buyer_bind_bankcard = value
    @property
    def buyer_bind_bankcard_type(self):
        return self._buyer_bind_bankcard_type

    @buyer_bind_bankcard_type.setter
    def buyer_bind_bankcard_type(self, value):
        self._buyer_bind_bankcard_type = value
    @property
    def buyer_bind_mobile(self):
        return self._buyer_bind_mobile

    @buyer_bind_mobile.setter
    def buyer_bind_mobile(self, value):
        self._buyer_bind_mobile = value
    @property
    def buyer_grade(self):
        return self._buyer_grade

    @buyer_grade.setter
    def buyer_grade(self, value):
        self._buyer_grade = value
    @property
    def buyer_identity_no(self):
        return self._buyer_identity_no

    @buyer_identity_no.setter
    def buyer_identity_no(self, value):
        self._buyer_identity_no = value
    @property
    def buyer_identity_type(self):
        return self._buyer_identity_type

    @buyer_identity_type.setter
    def buyer_identity_type(self, value):
        self._buyer_identity_type = value
    @property
    def buyer_real_name(self):
        return self._buyer_real_name

    @buyer_real_name.setter
    def buyer_real_name(self, value):
        self._buyer_real_name = value
    @property
    def buyer_reg_date(self):
        return self._buyer_reg_date

    @buyer_reg_date.setter
    def buyer_reg_date(self, value):
        self._buyer_reg_date = value
    @property
    def buyer_reg_email(self):
        return self._buyer_reg_email

    @buyer_reg_email.setter
    def buyer_reg_email(self, value):
        self._buyer_reg_email = value
    @property
    def buyer_reg_mobile(self):
        return self._buyer_reg_mobile

    @buyer_reg_mobile.setter
    def buyer_reg_mobile(self, value):
        self._buyer_reg_mobile = value
    @property
    def buyer_scene_bankcard(self):
        return self._buyer_scene_bankcard

    @buyer_scene_bankcard.setter
    def buyer_scene_bankcard(self, value):
        self._buyer_scene_bankcard = value
    @property
    def buyer_scene_bankcard_type(self):
        return self._buyer_scene_bankcard_type

    @buyer_scene_bankcard_type.setter
    def buyer_scene_bankcard_type(self, value):
        self._buyer_scene_bankcard_type = value
    @property
    def buyer_scene_email(self):
        return self._buyer_scene_email

    @buyer_scene_email.setter
    def buyer_scene_email(self, value):
        self._buyer_scene_email = value
    @property
    def buyer_scene_mobile(self):
        return self._buyer_scene_mobile

    @buyer_scene_mobile.setter
    def buyer_scene_mobile(self, value):
        self._buyer_scene_mobile = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def env_client_base_band(self):
        return self._env_client_base_band

    @env_client_base_band.setter
    def env_client_base_band(self, value):
        self._env_client_base_band = value
    @property
    def env_client_base_station(self):
        return self._env_client_base_station

    @env_client_base_station.setter
    def env_client_base_station(self, value):
        self._env_client_base_station = value
    @property
    def env_client_coordinates(self):
        return self._env_client_coordinates

    @env_client_coordinates.setter
    def env_client_coordinates(self, value):
        self._env_client_coordinates = value
    @property
    def env_client_imei(self):
        return self._env_client_imei

    @env_client_imei.setter
    def env_client_imei(self, value):
        self._env_client_imei = value
    @property
    def env_client_imsi(self):
        return self._env_client_imsi

    @env_client_imsi.setter
    def env_client_imsi(self, value):
        self._env_client_imsi = value
    @property
    def env_client_ios_udid(self):
        return self._env_client_ios_udid

    @env_client_ios_udid.setter
    def env_client_ios_udid(self, value):
        self._env_client_ios_udid = value
    @property
    def env_client_ip(self):
        return self._env_client_ip

    @env_client_ip.setter
    def env_client_ip(self, value):
        self._env_client_ip = value
    @property
    def env_client_mac(self):
        return self._env_client_mac

    @env_client_mac.setter
    def env_client_mac(self, value):
        self._env_client_mac = value
    @property
    def env_client_screen(self):
        return self._env_client_screen

    @env_client_screen.setter
    def env_client_screen(self, value):
        self._env_client_screen = value
    @property
    def env_client_uuid(self):
        return self._env_client_uuid

    @env_client_uuid.setter
    def env_client_uuid(self, value):
        self._env_client_uuid = value
    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value
    @property
    def item_unit_price(self):
        return self._item_unit_price

    @item_unit_price.setter
    def item_unit_price(self, value):
        self._item_unit_price = value
    @property
    def js_token_id(self):
        return self._js_token_id

    @js_token_id.setter
    def js_token_id(self, value):
        self._js_token_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_category(self):
        return self._order_category

    @order_category.setter
    def order_category(self, value):
        self._order_category = value
    @property
    def order_credate_time(self):
        return self._order_credate_time

    @order_credate_time.setter
    def order_credate_time(self, value):
        self._order_credate_time = value
    @property
    def order_item_city(self):
        return self._order_item_city

    @order_item_city.setter
    def order_item_city(self, value):
        self._order_item_city = value
    @property
    def order_item_name(self):
        return self._order_item_name

    @order_item_name.setter
    def order_item_name(self, value):
        self._order_item_name = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_city(self):
        return self._receiver_city

    @receiver_city.setter
    def receiver_city(self, value):
        self._receiver_city = value
    @property
    def receiver_district(self):
        return self._receiver_district

    @receiver_district.setter
    def receiver_district(self, value):
        self._receiver_district = value
    @property
    def receiver_email(self):
        return self._receiver_email

    @receiver_email.setter
    def receiver_email(self, value):
        self._receiver_email = value
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
    def receiver_state(self):
        return self._receiver_state

    @receiver_state.setter
    def receiver_state(self, value):
        self._receiver_state = value
    @property
    def receiver_zip(self):
        return self._receiver_zip

    @receiver_zip.setter
    def receiver_zip(self, value):
        self._receiver_zip = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def seller_account_no(self):
        return self._seller_account_no

    @seller_account_no.setter
    def seller_account_no(self, value):
        self._seller_account_no = value
    @property
    def seller_bind_bankcard(self):
        return self._seller_bind_bankcard

    @seller_bind_bankcard.setter
    def seller_bind_bankcard(self, value):
        self._seller_bind_bankcard = value
    @property
    def seller_bind_bankcard_type(self):
        return self._seller_bind_bankcard_type

    @seller_bind_bankcard_type.setter
    def seller_bind_bankcard_type(self, value):
        self._seller_bind_bankcard_type = value
    @property
    def seller_bind_mobile(self):
        return self._seller_bind_mobile

    @seller_bind_mobile.setter
    def seller_bind_mobile(self, value):
        self._seller_bind_mobile = value
    @property
    def seller_identity_no(self):
        return self._seller_identity_no

    @seller_identity_no.setter
    def seller_identity_no(self, value):
        self._seller_identity_no = value
    @property
    def seller_identity_type(self):
        return self._seller_identity_type

    @seller_identity_type.setter
    def seller_identity_type(self, value):
        self._seller_identity_type = value
    @property
    def seller_real_name(self):
        return self._seller_real_name

    @seller_real_name.setter
    def seller_real_name(self, value):
        self._seller_real_name = value
    @property
    def seller_reg_date(self):
        return self._seller_reg_date

    @seller_reg_date.setter
    def seller_reg_date(self, value):
        self._seller_reg_date = value
    @property
    def seller_reg_email(self):
        return self._seller_reg_email

    @seller_reg_email.setter
    def seller_reg_email(self, value):
        self._seller_reg_email = value
    @property
    def seller_reg_moile(self):
        return self._seller_reg_moile

    @seller_reg_moile.setter
    def seller_reg_moile(self, value):
        self._seller_reg_moile = value
    @property
    def transport_type(self):
        return self._transport_type

    @transport_type.setter
    def transport_type(self, value):
        self._transport_type = value


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.security.risk.detect'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.buyer_account_no:
            if hasattr(self.buyer_account_no, 'to_alipay_dict'):
                params['buyer_account_no'] = json.dumps(obj=self.buyer_account_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_account_no'] = self.buyer_account_no
        if self.buyer_bind_bankcard:
            if hasattr(self.buyer_bind_bankcard, 'to_alipay_dict'):
                params['buyer_bind_bankcard'] = json.dumps(obj=self.buyer_bind_bankcard.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_bind_bankcard'] = self.buyer_bind_bankcard
        if self.buyer_bind_bankcard_type:
            if hasattr(self.buyer_bind_bankcard_type, 'to_alipay_dict'):
                params['buyer_bind_bankcard_type'] = json.dumps(obj=self.buyer_bind_bankcard_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_bind_bankcard_type'] = self.buyer_bind_bankcard_type
        if self.buyer_bind_mobile:
            if hasattr(self.buyer_bind_mobile, 'to_alipay_dict'):
                params['buyer_bind_mobile'] = json.dumps(obj=self.buyer_bind_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_bind_mobile'] = self.buyer_bind_mobile
        if self.buyer_grade:
            if hasattr(self.buyer_grade, 'to_alipay_dict'):
                params['buyer_grade'] = json.dumps(obj=self.buyer_grade.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_grade'] = self.buyer_grade
        if self.buyer_identity_no:
            if hasattr(self.buyer_identity_no, 'to_alipay_dict'):
                params['buyer_identity_no'] = json.dumps(obj=self.buyer_identity_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_identity_no'] = self.buyer_identity_no
        if self.buyer_identity_type:
            if hasattr(self.buyer_identity_type, 'to_alipay_dict'):
                params['buyer_identity_type'] = json.dumps(obj=self.buyer_identity_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_identity_type'] = self.buyer_identity_type
        if self.buyer_real_name:
            if hasattr(self.buyer_real_name, 'to_alipay_dict'):
                params['buyer_real_name'] = json.dumps(obj=self.buyer_real_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_real_name'] = self.buyer_real_name
        if self.buyer_reg_date:
            if hasattr(self.buyer_reg_date, 'to_alipay_dict'):
                params['buyer_reg_date'] = json.dumps(obj=self.buyer_reg_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_reg_date'] = self.buyer_reg_date
        if self.buyer_reg_email:
            if hasattr(self.buyer_reg_email, 'to_alipay_dict'):
                params['buyer_reg_email'] = json.dumps(obj=self.buyer_reg_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_reg_email'] = self.buyer_reg_email
        if self.buyer_reg_mobile:
            if hasattr(self.buyer_reg_mobile, 'to_alipay_dict'):
                params['buyer_reg_mobile'] = json.dumps(obj=self.buyer_reg_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_reg_mobile'] = self.buyer_reg_mobile
        if self.buyer_scene_bankcard:
            if hasattr(self.buyer_scene_bankcard, 'to_alipay_dict'):
                params['buyer_scene_bankcard'] = json.dumps(obj=self.buyer_scene_bankcard.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_scene_bankcard'] = self.buyer_scene_bankcard
        if self.buyer_scene_bankcard_type:
            if hasattr(self.buyer_scene_bankcard_type, 'to_alipay_dict'):
                params['buyer_scene_bankcard_type'] = json.dumps(obj=self.buyer_scene_bankcard_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_scene_bankcard_type'] = self.buyer_scene_bankcard_type
        if self.buyer_scene_email:
            if hasattr(self.buyer_scene_email, 'to_alipay_dict'):
                params['buyer_scene_email'] = json.dumps(obj=self.buyer_scene_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_scene_email'] = self.buyer_scene_email
        if self.buyer_scene_mobile:
            if hasattr(self.buyer_scene_mobile, 'to_alipay_dict'):
                params['buyer_scene_mobile'] = json.dumps(obj=self.buyer_scene_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['buyer_scene_mobile'] = self.buyer_scene_mobile
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = json.dumps(obj=self.currency.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['currency'] = self.currency
        if self.env_client_base_band:
            if hasattr(self.env_client_base_band, 'to_alipay_dict'):
                params['env_client_base_band'] = json.dumps(obj=self.env_client_base_band.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_base_band'] = self.env_client_base_band
        if self.env_client_base_station:
            if hasattr(self.env_client_base_station, 'to_alipay_dict'):
                params['env_client_base_station'] = json.dumps(obj=self.env_client_base_station.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_base_station'] = self.env_client_base_station
        if self.env_client_coordinates:
            if hasattr(self.env_client_coordinates, 'to_alipay_dict'):
                params['env_client_coordinates'] = json.dumps(obj=self.env_client_coordinates.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_coordinates'] = self.env_client_coordinates
        if self.env_client_imei:
            if hasattr(self.env_client_imei, 'to_alipay_dict'):
                params['env_client_imei'] = json.dumps(obj=self.env_client_imei.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_imei'] = self.env_client_imei
        if self.env_client_imsi:
            if hasattr(self.env_client_imsi, 'to_alipay_dict'):
                params['env_client_imsi'] = json.dumps(obj=self.env_client_imsi.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_imsi'] = self.env_client_imsi
        if self.env_client_ios_udid:
            if hasattr(self.env_client_ios_udid, 'to_alipay_dict'):
                params['env_client_ios_udid'] = json.dumps(obj=self.env_client_ios_udid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_ios_udid'] = self.env_client_ios_udid
        if self.env_client_ip:
            if hasattr(self.env_client_ip, 'to_alipay_dict'):
                params['env_client_ip'] = json.dumps(obj=self.env_client_ip.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_ip'] = self.env_client_ip
        if self.env_client_mac:
            if hasattr(self.env_client_mac, 'to_alipay_dict'):
                params['env_client_mac'] = json.dumps(obj=self.env_client_mac.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_mac'] = self.env_client_mac
        if self.env_client_screen:
            if hasattr(self.env_client_screen, 'to_alipay_dict'):
                params['env_client_screen'] = json.dumps(obj=self.env_client_screen.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_screen'] = self.env_client_screen
        if self.env_client_uuid:
            if hasattr(self.env_client_uuid, 'to_alipay_dict'):
                params['env_client_uuid'] = json.dumps(obj=self.env_client_uuid.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['env_client_uuid'] = self.env_client_uuid
        if self.item_quantity:
            if hasattr(self.item_quantity, 'to_alipay_dict'):
                params['item_quantity'] = json.dumps(obj=self.item_quantity.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['item_quantity'] = self.item_quantity
        if self.item_unit_price:
            if hasattr(self.item_unit_price, 'to_alipay_dict'):
                params['item_unit_price'] = json.dumps(obj=self.item_unit_price.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['item_unit_price'] = self.item_unit_price
        if self.js_token_id:
            if hasattr(self.js_token_id, 'to_alipay_dict'):
                params['js_token_id'] = json.dumps(obj=self.js_token_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['js_token_id'] = self.js_token_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = json.dumps(obj=self.order_amount.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_amount'] = self.order_amount
        if self.order_category:
            if hasattr(self.order_category, 'to_alipay_dict'):
                params['order_category'] = json.dumps(obj=self.order_category.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_category'] = self.order_category
        if self.order_credate_time:
            if hasattr(self.order_credate_time, 'to_alipay_dict'):
                params['order_credate_time'] = json.dumps(obj=self.order_credate_time.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_credate_time'] = self.order_credate_time
        if self.order_item_city:
            if hasattr(self.order_item_city, 'to_alipay_dict'):
                params['order_item_city'] = json.dumps(obj=self.order_item_city.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_item_city'] = self.order_item_city
        if self.order_item_name:
            if hasattr(self.order_item_name, 'to_alipay_dict'):
                params['order_item_name'] = json.dumps(obj=self.order_item_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_item_name'] = self.order_item_name
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = json.dumps(obj=self.order_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['order_no'] = self.order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = json.dumps(obj=self.partner_id.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['partner_id'] = self.partner_id
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = json.dumps(obj=self.receiver_address.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_city:
            if hasattr(self.receiver_city, 'to_alipay_dict'):
                params['receiver_city'] = json.dumps(obj=self.receiver_city.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_city'] = self.receiver_city
        if self.receiver_district:
            if hasattr(self.receiver_district, 'to_alipay_dict'):
                params['receiver_district'] = json.dumps(obj=self.receiver_district.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_district'] = self.receiver_district
        if self.receiver_email:
            if hasattr(self.receiver_email, 'to_alipay_dict'):
                params['receiver_email'] = json.dumps(obj=self.receiver_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_email'] = self.receiver_email
        if self.receiver_mobile:
            if hasattr(self.receiver_mobile, 'to_alipay_dict'):
                params['receiver_mobile'] = json.dumps(obj=self.receiver_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_mobile'] = self.receiver_mobile
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = json.dumps(obj=self.receiver_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_state:
            if hasattr(self.receiver_state, 'to_alipay_dict'):
                params['receiver_state'] = json.dumps(obj=self.receiver_state.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_state'] = self.receiver_state
        if self.receiver_zip:
            if hasattr(self.receiver_zip, 'to_alipay_dict'):
                params['receiver_zip'] = json.dumps(obj=self.receiver_zip.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['receiver_zip'] = self.receiver_zip
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = json.dumps(obj=self.scene_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['scene_code'] = self.scene_code
        if self.seller_account_no:
            if hasattr(self.seller_account_no, 'to_alipay_dict'):
                params['seller_account_no'] = json.dumps(obj=self.seller_account_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_account_no'] = self.seller_account_no
        if self.seller_bind_bankcard:
            if hasattr(self.seller_bind_bankcard, 'to_alipay_dict'):
                params['seller_bind_bankcard'] = json.dumps(obj=self.seller_bind_bankcard.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_bind_bankcard'] = self.seller_bind_bankcard
        if self.seller_bind_bankcard_type:
            if hasattr(self.seller_bind_bankcard_type, 'to_alipay_dict'):
                params['seller_bind_bankcard_type'] = json.dumps(obj=self.seller_bind_bankcard_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_bind_bankcard_type'] = self.seller_bind_bankcard_type
        if self.seller_bind_mobile:
            if hasattr(self.seller_bind_mobile, 'to_alipay_dict'):
                params['seller_bind_mobile'] = json.dumps(obj=self.seller_bind_mobile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_bind_mobile'] = self.seller_bind_mobile
        if self.seller_identity_no:
            if hasattr(self.seller_identity_no, 'to_alipay_dict'):
                params['seller_identity_no'] = json.dumps(obj=self.seller_identity_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_identity_no'] = self.seller_identity_no
        if self.seller_identity_type:
            if hasattr(self.seller_identity_type, 'to_alipay_dict'):
                params['seller_identity_type'] = json.dumps(obj=self.seller_identity_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_identity_type'] = self.seller_identity_type
        if self.seller_real_name:
            if hasattr(self.seller_real_name, 'to_alipay_dict'):
                params['seller_real_name'] = json.dumps(obj=self.seller_real_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_real_name'] = self.seller_real_name
        if self.seller_reg_date:
            if hasattr(self.seller_reg_date, 'to_alipay_dict'):
                params['seller_reg_date'] = json.dumps(obj=self.seller_reg_date.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_reg_date'] = self.seller_reg_date
        if self.seller_reg_email:
            if hasattr(self.seller_reg_email, 'to_alipay_dict'):
                params['seller_reg_email'] = json.dumps(obj=self.seller_reg_email.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_reg_email'] = self.seller_reg_email
        if self.seller_reg_moile:
            if hasattr(self.seller_reg_moile, 'to_alipay_dict'):
                params['seller_reg_moile'] = json.dumps(obj=self.seller_reg_moile.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_reg_moile'] = self.seller_reg_moile
        if self.transport_type:
            if hasattr(self.transport_type, 'to_alipay_dict'):
                params['transport_type'] = json.dumps(obj=self.transport_type.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['transport_type'] = self.transport_type
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        return multipart_params
