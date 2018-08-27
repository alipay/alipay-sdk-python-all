#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayEcoRenthouseBookInfo import AlipayEcoRenthouseBookInfo


class AlipayEcoRenthouseLeaseOrderSyncModel(object):

    def __init__(self):
        self._attach_file = None
        self._begin_date = None
        self._book_info = None
        self._card_no = None
        self._card_type = None
        self._end_date = None
        self._flats_tag = None
        self._foregift_amount = None
        self._free_deposit = None
        self._furniture_items = None
        self._images = None
        self._lease_code = None
        self._lease_create_time = None
        self._lease_status = None
        self._lease_type = None
        self._original_lease_code = None
        self._other_fee_desc = None
        self._pay_type = None
        self._rebate_amount = None
        self._remark = None
        self._renew_lease = None
        self._renew_num = None
        self._rent_day_desc = None
        self._rent_include_fee_desc = None
        self._renter_gender = None
        self._renter_name = None
        self._renter_phone = None
        self._room_code = None
        self._room_num = None
        self._sale_amount = None

    @property
    def attach_file(self):
        return self._attach_file

    @attach_file.setter
    def attach_file(self, value):
        self._attach_file = value
    @property
    def begin_date(self):
        return self._begin_date

    @begin_date.setter
    def begin_date(self, value):
        self._begin_date = value
    @property
    def book_info(self):
        return self._book_info

    @book_info.setter
    def book_info(self, value):
        if isinstance(value, AlipayEcoRenthouseBookInfo):
            self._book_info = value
        else:
            self._book_info = AlipayEcoRenthouseBookInfo.from_alipay_dict(value)
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def flats_tag(self):
        return self._flats_tag

    @flats_tag.setter
    def flats_tag(self, value):
        self._flats_tag = value
    @property
    def foregift_amount(self):
        return self._foregift_amount

    @foregift_amount.setter
    def foregift_amount(self, value):
        self._foregift_amount = value
    @property
    def free_deposit(self):
        return self._free_deposit

    @free_deposit.setter
    def free_deposit(self, value):
        self._free_deposit = value
    @property
    def furniture_items(self):
        return self._furniture_items

    @furniture_items.setter
    def furniture_items(self, value):
        self._furniture_items = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value
    @property
    def lease_code(self):
        return self._lease_code

    @lease_code.setter
    def lease_code(self, value):
        self._lease_code = value
    @property
    def lease_create_time(self):
        return self._lease_create_time

    @lease_create_time.setter
    def lease_create_time(self, value):
        self._lease_create_time = value
    @property
    def lease_status(self):
        return self._lease_status

    @lease_status.setter
    def lease_status(self, value):
        self._lease_status = value
    @property
    def lease_type(self):
        return self._lease_type

    @lease_type.setter
    def lease_type(self, value):
        self._lease_type = value
    @property
    def original_lease_code(self):
        return self._original_lease_code

    @original_lease_code.setter
    def original_lease_code(self, value):
        self._original_lease_code = value
    @property
    def other_fee_desc(self):
        return self._other_fee_desc

    @other_fee_desc.setter
    def other_fee_desc(self, value):
        self._other_fee_desc = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def rebate_amount(self):
        return self._rebate_amount

    @rebate_amount.setter
    def rebate_amount(self, value):
        self._rebate_amount = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def renew_lease(self):
        return self._renew_lease

    @renew_lease.setter
    def renew_lease(self, value):
        self._renew_lease = value
    @property
    def renew_num(self):
        return self._renew_num

    @renew_num.setter
    def renew_num(self, value):
        self._renew_num = value
    @property
    def rent_day_desc(self):
        return self._rent_day_desc

    @rent_day_desc.setter
    def rent_day_desc(self, value):
        self._rent_day_desc = value
    @property
    def rent_include_fee_desc(self):
        return self._rent_include_fee_desc

    @rent_include_fee_desc.setter
    def rent_include_fee_desc(self, value):
        if isinstance(value, list):
            self._rent_include_fee_desc = list()
            for i in value:
                self._rent_include_fee_desc.append(i)
    @property
    def renter_gender(self):
        return self._renter_gender

    @renter_gender.setter
    def renter_gender(self, value):
        self._renter_gender = value
    @property
    def renter_name(self):
        return self._renter_name

    @renter_name.setter
    def renter_name(self, value):
        self._renter_name = value
    @property
    def renter_phone(self):
        return self._renter_phone

    @renter_phone.setter
    def renter_phone(self, value):
        self._renter_phone = value
    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        self._room_code = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value
    @property
    def sale_amount(self):
        return self._sale_amount

    @sale_amount.setter
    def sale_amount(self, value):
        self._sale_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.attach_file:
            if hasattr(self.attach_file, 'to_alipay_dict'):
                params['attach_file'] = self.attach_file.to_alipay_dict()
            else:
                params['attach_file'] = self.attach_file
        if self.begin_date:
            if hasattr(self.begin_date, 'to_alipay_dict'):
                params['begin_date'] = self.begin_date.to_alipay_dict()
            else:
                params['begin_date'] = self.begin_date
        if self.book_info:
            if hasattr(self.book_info, 'to_alipay_dict'):
                params['book_info'] = self.book_info.to_alipay_dict()
            else:
                params['book_info'] = self.book_info
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.flats_tag:
            if hasattr(self.flats_tag, 'to_alipay_dict'):
                params['flats_tag'] = self.flats_tag.to_alipay_dict()
            else:
                params['flats_tag'] = self.flats_tag
        if self.foregift_amount:
            if hasattr(self.foregift_amount, 'to_alipay_dict'):
                params['foregift_amount'] = self.foregift_amount.to_alipay_dict()
            else:
                params['foregift_amount'] = self.foregift_amount
        if self.free_deposit:
            if hasattr(self.free_deposit, 'to_alipay_dict'):
                params['free_deposit'] = self.free_deposit.to_alipay_dict()
            else:
                params['free_deposit'] = self.free_deposit
        if self.furniture_items:
            if hasattr(self.furniture_items, 'to_alipay_dict'):
                params['furniture_items'] = self.furniture_items.to_alipay_dict()
            else:
                params['furniture_items'] = self.furniture_items
        if self.images:
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.lease_code:
            if hasattr(self.lease_code, 'to_alipay_dict'):
                params['lease_code'] = self.lease_code.to_alipay_dict()
            else:
                params['lease_code'] = self.lease_code
        if self.lease_create_time:
            if hasattr(self.lease_create_time, 'to_alipay_dict'):
                params['lease_create_time'] = self.lease_create_time.to_alipay_dict()
            else:
                params['lease_create_time'] = self.lease_create_time
        if self.lease_status:
            if hasattr(self.lease_status, 'to_alipay_dict'):
                params['lease_status'] = self.lease_status.to_alipay_dict()
            else:
                params['lease_status'] = self.lease_status
        if self.lease_type:
            if hasattr(self.lease_type, 'to_alipay_dict'):
                params['lease_type'] = self.lease_type.to_alipay_dict()
            else:
                params['lease_type'] = self.lease_type
        if self.original_lease_code:
            if hasattr(self.original_lease_code, 'to_alipay_dict'):
                params['original_lease_code'] = self.original_lease_code.to_alipay_dict()
            else:
                params['original_lease_code'] = self.original_lease_code
        if self.other_fee_desc:
            if hasattr(self.other_fee_desc, 'to_alipay_dict'):
                params['other_fee_desc'] = self.other_fee_desc.to_alipay_dict()
            else:
                params['other_fee_desc'] = self.other_fee_desc
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.rebate_amount:
            if hasattr(self.rebate_amount, 'to_alipay_dict'):
                params['rebate_amount'] = self.rebate_amount.to_alipay_dict()
            else:
                params['rebate_amount'] = self.rebate_amount
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.renew_lease:
            if hasattr(self.renew_lease, 'to_alipay_dict'):
                params['renew_lease'] = self.renew_lease.to_alipay_dict()
            else:
                params['renew_lease'] = self.renew_lease
        if self.renew_num:
            if hasattr(self.renew_num, 'to_alipay_dict'):
                params['renew_num'] = self.renew_num.to_alipay_dict()
            else:
                params['renew_num'] = self.renew_num
        if self.rent_day_desc:
            if hasattr(self.rent_day_desc, 'to_alipay_dict'):
                params['rent_day_desc'] = self.rent_day_desc.to_alipay_dict()
            else:
                params['rent_day_desc'] = self.rent_day_desc
        if self.rent_include_fee_desc:
            if isinstance(self.rent_include_fee_desc, list):
                for i in range(0, len(self.rent_include_fee_desc)):
                    element = self.rent_include_fee_desc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.rent_include_fee_desc[i] = element.to_alipay_dict()
            if hasattr(self.rent_include_fee_desc, 'to_alipay_dict'):
                params['rent_include_fee_desc'] = self.rent_include_fee_desc.to_alipay_dict()
            else:
                params['rent_include_fee_desc'] = self.rent_include_fee_desc
        if self.renter_gender:
            if hasattr(self.renter_gender, 'to_alipay_dict'):
                params['renter_gender'] = self.renter_gender.to_alipay_dict()
            else:
                params['renter_gender'] = self.renter_gender
        if self.renter_name:
            if hasattr(self.renter_name, 'to_alipay_dict'):
                params['renter_name'] = self.renter_name.to_alipay_dict()
            else:
                params['renter_name'] = self.renter_name
        if self.renter_phone:
            if hasattr(self.renter_phone, 'to_alipay_dict'):
                params['renter_phone'] = self.renter_phone.to_alipay_dict()
            else:
                params['renter_phone'] = self.renter_phone
        if self.room_code:
            if hasattr(self.room_code, 'to_alipay_dict'):
                params['room_code'] = self.room_code.to_alipay_dict()
            else:
                params['room_code'] = self.room_code
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        if self.sale_amount:
            if hasattr(self.sale_amount, 'to_alipay_dict'):
                params['sale_amount'] = self.sale_amount.to_alipay_dict()
            else:
                params['sale_amount'] = self.sale_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseLeaseOrderSyncModel()
        if 'attach_file' in d:
            o.attach_file = d['attach_file']
        if 'begin_date' in d:
            o.begin_date = d['begin_date']
        if 'book_info' in d:
            o.book_info = d['book_info']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'flats_tag' in d:
            o.flats_tag = d['flats_tag']
        if 'foregift_amount' in d:
            o.foregift_amount = d['foregift_amount']
        if 'free_deposit' in d:
            o.free_deposit = d['free_deposit']
        if 'furniture_items' in d:
            o.furniture_items = d['furniture_items']
        if 'images' in d:
            o.images = d['images']
        if 'lease_code' in d:
            o.lease_code = d['lease_code']
        if 'lease_create_time' in d:
            o.lease_create_time = d['lease_create_time']
        if 'lease_status' in d:
            o.lease_status = d['lease_status']
        if 'lease_type' in d:
            o.lease_type = d['lease_type']
        if 'original_lease_code' in d:
            o.original_lease_code = d['original_lease_code']
        if 'other_fee_desc' in d:
            o.other_fee_desc = d['other_fee_desc']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'rebate_amount' in d:
            o.rebate_amount = d['rebate_amount']
        if 'remark' in d:
            o.remark = d['remark']
        if 'renew_lease' in d:
            o.renew_lease = d['renew_lease']
        if 'renew_num' in d:
            o.renew_num = d['renew_num']
        if 'rent_day_desc' in d:
            o.rent_day_desc = d['rent_day_desc']
        if 'rent_include_fee_desc' in d:
            o.rent_include_fee_desc = d['rent_include_fee_desc']
        if 'renter_gender' in d:
            o.renter_gender = d['renter_gender']
        if 'renter_name' in d:
            o.renter_name = d['renter_name']
        if 'renter_phone' in d:
            o.renter_phone = d['renter_phone']
        if 'room_code' in d:
            o.room_code = d['room_code']
        if 'room_num' in d:
            o.room_num = d['room_num']
        if 'sale_amount' in d:
            o.sale_amount = d['sale_amount']
        return o


