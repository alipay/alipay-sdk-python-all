#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LubBusinessLicenseInfo import LubBusinessLicenseInfo
from alipay.aop.api.domain.LubContactWayInfo import LubContactWayInfo
from alipay.aop.api.domain.LubLegalPersonInfo import LubLegalPersonInfo
from alipay.aop.api.domain.LubStoreAddressInfo import LubStoreAddressInfo


class LubUnifiedShopListQueryItem(object):

    def __init__(self):
        self._brand_id = None
        self._business_license_info = None
        self._contact_ways = None
        self._gmt_create = None
        self._gmt_modified = None
        self._legal_person_info = None
        self._qualification_business_license = None
        self._qualification_certificates = None
        self._qualification_expiration_date = None
        self._qualification_type = None
        self._shop_category = None
        self._shop_category_name = None
        self._shop_id = None
        self._shop_name = None
        self._shop_type = None
        self._status = None
        self._store_address_info = None
        self._store_id = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def business_license_info(self):
        return self._business_license_info

    @business_license_info.setter
    def business_license_info(self, value):
        if isinstance(value, LubBusinessLicenseInfo):
            self._business_license_info = value
        else:
            self._business_license_info = LubBusinessLicenseInfo.from_alipay_dict(value)
    @property
    def contact_ways(self):
        return self._contact_ways

    @contact_ways.setter
    def contact_ways(self, value):
        if isinstance(value, list):
            self._contact_ways = list()
            for i in value:
                if isinstance(i, LubContactWayInfo):
                    self._contact_ways.append(i)
                else:
                    self._contact_ways.append(LubContactWayInfo.from_alipay_dict(i))
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def legal_person_info(self):
        return self._legal_person_info

    @legal_person_info.setter
    def legal_person_info(self, value):
        if isinstance(value, LubLegalPersonInfo):
            self._legal_person_info = value
        else:
            self._legal_person_info = LubLegalPersonInfo.from_alipay_dict(value)
    @property
    def qualification_business_license(self):
        return self._qualification_business_license

    @qualification_business_license.setter
    def qualification_business_license(self, value):
        self._qualification_business_license = value
    @property
    def qualification_certificates(self):
        return self._qualification_certificates

    @qualification_certificates.setter
    def qualification_certificates(self, value):
        self._qualification_certificates = value
    @property
    def qualification_expiration_date(self):
        return self._qualification_expiration_date

    @qualification_expiration_date.setter
    def qualification_expiration_date(self, value):
        self._qualification_expiration_date = value
    @property
    def qualification_type(self):
        return self._qualification_type

    @qualification_type.setter
    def qualification_type(self, value):
        self._qualification_type = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_category_name(self):
        return self._shop_category_name

    @shop_category_name.setter
    def shop_category_name(self, value):
        self._shop_category_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_address_info(self):
        return self._store_address_info

    @store_address_info.setter
    def store_address_info(self, value):
        if isinstance(value, LubStoreAddressInfo):
            self._store_address_info = value
        else:
            self._store_address_info = LubStoreAddressInfo.from_alipay_dict(value)
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.business_license_info:
            if hasattr(self.business_license_info, 'to_alipay_dict'):
                params['business_license_info'] = self.business_license_info.to_alipay_dict()
            else:
                params['business_license_info'] = self.business_license_info
        if self.contact_ways:
            if isinstance(self.contact_ways, list):
                for i in range(0, len(self.contact_ways)):
                    element = self.contact_ways[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_ways[i] = element.to_alipay_dict()
            if hasattr(self.contact_ways, 'to_alipay_dict'):
                params['contact_ways'] = self.contact_ways.to_alipay_dict()
            else:
                params['contact_ways'] = self.contact_ways
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.legal_person_info:
            if hasattr(self.legal_person_info, 'to_alipay_dict'):
                params['legal_person_info'] = self.legal_person_info.to_alipay_dict()
            else:
                params['legal_person_info'] = self.legal_person_info
        if self.qualification_business_license:
            if hasattr(self.qualification_business_license, 'to_alipay_dict'):
                params['qualification_business_license'] = self.qualification_business_license.to_alipay_dict()
            else:
                params['qualification_business_license'] = self.qualification_business_license
        if self.qualification_certificates:
            if hasattr(self.qualification_certificates, 'to_alipay_dict'):
                params['qualification_certificates'] = self.qualification_certificates.to_alipay_dict()
            else:
                params['qualification_certificates'] = self.qualification_certificates
        if self.qualification_expiration_date:
            if hasattr(self.qualification_expiration_date, 'to_alipay_dict'):
                params['qualification_expiration_date'] = self.qualification_expiration_date.to_alipay_dict()
            else:
                params['qualification_expiration_date'] = self.qualification_expiration_date
        if self.qualification_type:
            if hasattr(self.qualification_type, 'to_alipay_dict'):
                params['qualification_type'] = self.qualification_type.to_alipay_dict()
            else:
                params['qualification_type'] = self.qualification_type
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_category_name:
            if hasattr(self.shop_category_name, 'to_alipay_dict'):
                params['shop_category_name'] = self.shop_category_name.to_alipay_dict()
            else:
                params['shop_category_name'] = self.shop_category_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_address_info:
            if hasattr(self.store_address_info, 'to_alipay_dict'):
                params['store_address_info'] = self.store_address_info.to_alipay_dict()
            else:
                params['store_address_info'] = self.store_address_info
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LubUnifiedShopListQueryItem()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'business_license_info' in d:
            o.business_license_info = d['business_license_info']
        if 'contact_ways' in d:
            o.contact_ways = d['contact_ways']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'legal_person_info' in d:
            o.legal_person_info = d['legal_person_info']
        if 'qualification_business_license' in d:
            o.qualification_business_license = d['qualification_business_license']
        if 'qualification_certificates' in d:
            o.qualification_certificates = d['qualification_certificates']
        if 'qualification_expiration_date' in d:
            o.qualification_expiration_date = d['qualification_expiration_date']
        if 'qualification_type' in d:
            o.qualification_type = d['qualification_type']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_category_name' in d:
            o.shop_category_name = d['shop_category_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'status' in d:
            o.status = d['status']
        if 'store_address_info' in d:
            o.store_address_info = d['store_address_info']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


