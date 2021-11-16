#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantSiteInfo import MerchantSiteInfo


class AlipayOverseasSecondmerchantOnlineMaintainModel(object):

    def __init__(self):
        self._contact_email = None
        self._contact_no = None
        self._cs_email = None
        self._cs_no = None
        self._register_address = None
        self._register_country = None
        self._registration_no = None
        self._representative_id = None
        self._representative_name = None
        self._representative_nationality = None
        self._secondary_merchant_id = None
        self._secondary_merchant_industry = None
        self._secondary_merchant_name = None
        self._secondary_merchant_type = None
        self._settlement_no = None
        self._shareholder_id = None
        self._shareholder_name = None
        self._shareholder_nationality = None
        self._site_infos = None

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
    def secondary_merchant_industry(self):
        return self._secondary_merchant_industry

    @secondary_merchant_industry.setter
    def secondary_merchant_industry(self, value):
        self._secondary_merchant_industry = value
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
    def site_infos(self):
        return self._site_infos

    @site_infos.setter
    def site_infos(self, value):
        if isinstance(value, list):
            self._site_infos = list()
            for i in value:
                if isinstance(i, MerchantSiteInfo):
                    self._site_infos.append(i)
                else:
                    self._site_infos.append(MerchantSiteInfo.from_alipay_dict(i))


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
        if self.secondary_merchant_industry:
            if hasattr(self.secondary_merchant_industry, 'to_alipay_dict'):
                params['secondary_merchant_industry'] = self.secondary_merchant_industry.to_alipay_dict()
            else:
                params['secondary_merchant_industry'] = self.secondary_merchant_industry
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
        if self.site_infos:
            if isinstance(self.site_infos, list):
                for i in range(0, len(self.site_infos)):
                    element = self.site_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.site_infos[i] = element.to_alipay_dict()
            if hasattr(self.site_infos, 'to_alipay_dict'):
                params['site_infos'] = self.site_infos.to_alipay_dict()
            else:
                params['site_infos'] = self.site_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasSecondmerchantOnlineMaintainModel()
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_no' in d:
            o.contact_no = d['contact_no']
        if 'cs_email' in d:
            o.cs_email = d['cs_email']
        if 'cs_no' in d:
            o.cs_no = d['cs_no']
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
        if 'secondary_merchant_industry' in d:
            o.secondary_merchant_industry = d['secondary_merchant_industry']
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
        if 'site_infos' in d:
            o.site_infos = d['site_infos']
        return o


