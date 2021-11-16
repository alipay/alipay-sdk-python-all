#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasSecondmerchantOfflineMaintainModel(object):

    def __init__(self):
        self._contact_email = None
        self._contact_no = None
        self._cs_email = None
        self._cs_no = None
        self._external_storefront_photo = None
        self._internal_store_photo = None
        self._register_address = None
        self._register_country = None
        self._registration_no = None
        self._representative_id = None
        self._representative_name = None
        self._representative_nationality = None
        self._secondary_merchant_id = None
        self._secondary_merchant_name = None
        self._secondary_merchant_type = None
        self._settlement_no = None
        self._shareholder_id = None
        self._shareholder_name = None
        self._shareholder_nationality = None
        self._store_address = None
        self._store_city = None
        self._store_country = None
        self._store_id = None
        self._store_industry = None
        self._store_name = None

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_no(self):
        return self._contact_no

    @contact_no.setter
    def contact_no(self, value):
        self._contact_no = value
    @property
    def cs_email(self):
        return self._cs_email

    @cs_email.setter
    def cs_email(self, value):
        self._cs_email = value
    @property
    def cs_no(self):
        return self._cs_no

    @cs_no.setter
    def cs_no(self, value):
        self._cs_no = value
    @property
    def external_storefront_photo(self):
        return self._external_storefront_photo

    @external_storefront_photo.setter
    def external_storefront_photo(self, value):
        self._external_storefront_photo = value
    @property
    def internal_store_photo(self):
        return self._internal_store_photo

    @internal_store_photo.setter
    def internal_store_photo(self, value):
        self._internal_store_photo = value
    @property
    def register_address(self):
        return self._register_address

    @register_address.setter
    def register_address(self, value):
        self._register_address = value
    @property
    def register_country(self):
        return self._register_country

    @register_country.setter
    def register_country(self, value):
        self._register_country = value
    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value
    @property
    def representative_id(self):
        return self._representative_id

    @representative_id.setter
    def representative_id(self, value):
        self._representative_id = value
    @property
    def representative_name(self):
        return self._representative_name

    @representative_name.setter
    def representative_name(self, value):
        self._representative_name = value
    @property
    def representative_nationality(self):
        return self._representative_nationality

    @representative_nationality.setter
    def representative_nationality(self, value):
        self._representative_nationality = value
    @property
    def secondary_merchant_id(self):
        return self._secondary_merchant_id

    @secondary_merchant_id.setter
    def secondary_merchant_id(self, value):
        self._secondary_merchant_id = value
    @property
    def secondary_merchant_name(self):
        return self._secondary_merchant_name

    @secondary_merchant_name.setter
    def secondary_merchant_name(self, value):
        self._secondary_merchant_name = value
    @property
    def secondary_merchant_type(self):
        return self._secondary_merchant_type

    @secondary_merchant_type.setter
    def secondary_merchant_type(self, value):
        self._secondary_merchant_type = value
    @property
    def settlement_no(self):
        return self._settlement_no

    @settlement_no.setter
    def settlement_no(self, value):
        self._settlement_no = value
    @property
    def shareholder_id(self):
        return self._shareholder_id

    @shareholder_id.setter
    def shareholder_id(self, value):
        self._shareholder_id = value
    @property
    def shareholder_name(self):
        return self._shareholder_name

    @shareholder_name.setter
    def shareholder_name(self, value):
        self._shareholder_name = value
    @property
    def shareholder_nationality(self):
        return self._shareholder_nationality

    @shareholder_nationality.setter
    def shareholder_nationality(self, value):
        self._shareholder_nationality = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_city(self):
        return self._store_city

    @store_city.setter
    def store_city(self, value):
        self._store_city = value
    @property
    def store_country(self):
        return self._store_country

    @store_country.setter
    def store_country(self, value):
        self._store_country = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_industry(self):
        return self._store_industry

    @store_industry.setter
    def store_industry(self, value):
        self._store_industry = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_no:
            if hasattr(self.contact_no, 'to_alipay_dict'):
                params['contact_no'] = self.contact_no.to_alipay_dict()
            else:
                params['contact_no'] = self.contact_no
        if self.cs_email:
            if hasattr(self.cs_email, 'to_alipay_dict'):
                params['cs_email'] = self.cs_email.to_alipay_dict()
            else:
                params['cs_email'] = self.cs_email
        if self.cs_no:
            if hasattr(self.cs_no, 'to_alipay_dict'):
                params['cs_no'] = self.cs_no.to_alipay_dict()
            else:
                params['cs_no'] = self.cs_no
        if self.external_storefront_photo:
            if hasattr(self.external_storefront_photo, 'to_alipay_dict'):
                params['external_storefront_photo'] = self.external_storefront_photo.to_alipay_dict()
            else:
                params['external_storefront_photo'] = self.external_storefront_photo
        if self.internal_store_photo:
            if hasattr(self.internal_store_photo, 'to_alipay_dict'):
                params['internal_store_photo'] = self.internal_store_photo.to_alipay_dict()
            else:
                params['internal_store_photo'] = self.internal_store_photo
        if self.register_address:
            if hasattr(self.register_address, 'to_alipay_dict'):
                params['register_address'] = self.register_address.to_alipay_dict()
            else:
                params['register_address'] = self.register_address
        if self.register_country:
            if hasattr(self.register_country, 'to_alipay_dict'):
                params['register_country'] = self.register_country.to_alipay_dict()
            else:
                params['register_country'] = self.register_country
        if self.registration_no:
            if hasattr(self.registration_no, 'to_alipay_dict'):
                params['registration_no'] = self.registration_no.to_alipay_dict()
            else:
                params['registration_no'] = self.registration_no
        if self.representative_id:
            if hasattr(self.representative_id, 'to_alipay_dict'):
                params['representative_id'] = self.representative_id.to_alipay_dict()
            else:
                params['representative_id'] = self.representative_id
        if self.representative_name:
            if hasattr(self.representative_name, 'to_alipay_dict'):
                params['representative_name'] = self.representative_name.to_alipay_dict()
            else:
                params['representative_name'] = self.representative_name
        if self.representative_nationality:
            if hasattr(self.representative_nationality, 'to_alipay_dict'):
                params['representative_nationality'] = self.representative_nationality.to_alipay_dict()
            else:
                params['representative_nationality'] = self.representative_nationality
        if self.secondary_merchant_id:
            if hasattr(self.secondary_merchant_id, 'to_alipay_dict'):
                params['secondary_merchant_id'] = self.secondary_merchant_id.to_alipay_dict()
            else:
                params['secondary_merchant_id'] = self.secondary_merchant_id
        if self.secondary_merchant_name:
            if hasattr(self.secondary_merchant_name, 'to_alipay_dict'):
                params['secondary_merchant_name'] = self.secondary_merchant_name.to_alipay_dict()
            else:
                params['secondary_merchant_name'] = self.secondary_merchant_name
        if self.secondary_merchant_type:
            if hasattr(self.secondary_merchant_type, 'to_alipay_dict'):
                params['secondary_merchant_type'] = self.secondary_merchant_type.to_alipay_dict()
            else:
                params['secondary_merchant_type'] = self.secondary_merchant_type
        if self.settlement_no:
            if hasattr(self.settlement_no, 'to_alipay_dict'):
                params['settlement_no'] = self.settlement_no.to_alipay_dict()
            else:
                params['settlement_no'] = self.settlement_no
        if self.shareholder_id:
            if hasattr(self.shareholder_id, 'to_alipay_dict'):
                params['shareholder_id'] = self.shareholder_id.to_alipay_dict()
            else:
                params['shareholder_id'] = self.shareholder_id
        if self.shareholder_name:
            if hasattr(self.shareholder_name, 'to_alipay_dict'):
                params['shareholder_name'] = self.shareholder_name.to_alipay_dict()
            else:
                params['shareholder_name'] = self.shareholder_name
        if self.shareholder_nationality:
            if hasattr(self.shareholder_nationality, 'to_alipay_dict'):
                params['shareholder_nationality'] = self.shareholder_nationality.to_alipay_dict()
            else:
                params['shareholder_nationality'] = self.shareholder_nationality
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_city:
            if hasattr(self.store_city, 'to_alipay_dict'):
                params['store_city'] = self.store_city.to_alipay_dict()
            else:
                params['store_city'] = self.store_city
        if self.store_country:
            if hasattr(self.store_country, 'to_alipay_dict'):
                params['store_country'] = self.store_country.to_alipay_dict()
            else:
                params['store_country'] = self.store_country
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_industry:
            if hasattr(self.store_industry, 'to_alipay_dict'):
                params['store_industry'] = self.store_industry.to_alipay_dict()
            else:
                params['store_industry'] = self.store_industry
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasSecondmerchantOfflineMaintainModel()
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_no' in d:
            o.contact_no = d['contact_no']
        if 'cs_email' in d:
            o.cs_email = d['cs_email']
        if 'cs_no' in d:
            o.cs_no = d['cs_no']
        if 'external_storefront_photo' in d:
            o.external_storefront_photo = d['external_storefront_photo']
        if 'internal_store_photo' in d:
            o.internal_store_photo = d['internal_store_photo']
        if 'register_address' in d:
            o.register_address = d['register_address']
        if 'register_country' in d:
            o.register_country = d['register_country']
        if 'registration_no' in d:
            o.registration_no = d['registration_no']
        if 'representative_id' in d:
            o.representative_id = d['representative_id']
        if 'representative_name' in d:
            o.representative_name = d['representative_name']
        if 'representative_nationality' in d:
            o.representative_nationality = d['representative_nationality']
        if 'secondary_merchant_id' in d:
            o.secondary_merchant_id = d['secondary_merchant_id']
        if 'secondary_merchant_name' in d:
            o.secondary_merchant_name = d['secondary_merchant_name']
        if 'secondary_merchant_type' in d:
            o.secondary_merchant_type = d['secondary_merchant_type']
        if 'settlement_no' in d:
            o.settlement_no = d['settlement_no']
        if 'shareholder_id' in d:
            o.shareholder_id = d['shareholder_id']
        if 'shareholder_name' in d:
            o.shareholder_name = d['shareholder_name']
        if 'shareholder_nationality' in d:
            o.shareholder_nationality = d['shareholder_nationality']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_city' in d:
            o.store_city = d['store_city']
        if 'store_country' in d:
            o.store_country = d['store_country']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_industry' in d:
            o.store_industry = d['store_industry']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


