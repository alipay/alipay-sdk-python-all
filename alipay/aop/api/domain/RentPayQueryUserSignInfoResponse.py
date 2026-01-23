#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayQueryUserSignInfoResponse(object):

    def __init__(self):
        self._applicant_id = None
        self._approval_status = None
        self._balance_amount = None
        self._biz_no = None
        self._draw_amount = None
        self._draw_interest = None
        self._draw_item = None
        self._draw_item_detail_id = None
        self._is_coextract = None
        self._item_creation_time = None
        self._item_id = None
        self._item_state = None
        self._operating_deck = None
        self._operating_time = None
        self._operator = None
        self._rent_monthly_balance = None
        self._rental_type = None
        self._trans_provincial_label = None
        self._user_record_no = None

    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        self._applicant_id = value
    @property
    def approval_status(self):
        return self._approval_status

    @approval_status.setter
    def approval_status(self, value):
        self._approval_status = value
    @property
    def balance_amount(self):
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, value):
        self._balance_amount = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def draw_amount(self):
        return self._draw_amount

    @draw_amount.setter
    def draw_amount(self, value):
        self._draw_amount = value
    @property
    def draw_interest(self):
        return self._draw_interest

    @draw_interest.setter
    def draw_interest(self, value):
        self._draw_interest = value
    @property
    def draw_item(self):
        return self._draw_item

    @draw_item.setter
    def draw_item(self, value):
        self._draw_item = value
    @property
    def draw_item_detail_id(self):
        return self._draw_item_detail_id

    @draw_item_detail_id.setter
    def draw_item_detail_id(self, value):
        self._draw_item_detail_id = value
    @property
    def is_coextract(self):
        return self._is_coextract

    @is_coextract.setter
    def is_coextract(self, value):
        self._is_coextract = value
    @property
    def item_creation_time(self):
        return self._item_creation_time

    @item_creation_time.setter
    def item_creation_time(self, value):
        self._item_creation_time = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_state(self):
        return self._item_state

    @item_state.setter
    def item_state(self, value):
        self._item_state = value
    @property
    def operating_deck(self):
        return self._operating_deck

    @operating_deck.setter
    def operating_deck(self, value):
        self._operating_deck = value
    @property
    def operating_time(self):
        return self._operating_time

    @operating_time.setter
    def operating_time(self, value):
        self._operating_time = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def rent_monthly_balance(self):
        return self._rent_monthly_balance

    @rent_monthly_balance.setter
    def rent_monthly_balance(self, value):
        self._rent_monthly_balance = value
    @property
    def rental_type(self):
        return self._rental_type

    @rental_type.setter
    def rental_type(self, value):
        self._rental_type = value
    @property
    def trans_provincial_label(self):
        return self._trans_provincial_label

    @trans_provincial_label.setter
    def trans_provincial_label(self, value):
        self._trans_provincial_label = value
    @property
    def user_record_no(self):
        return self._user_record_no

    @user_record_no.setter
    def user_record_no(self, value):
        self._user_record_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicant_id:
            if hasattr(self.applicant_id, 'to_alipay_dict'):
                params['applicant_id'] = self.applicant_id.to_alipay_dict()
            else:
                params['applicant_id'] = self.applicant_id
        if self.approval_status:
            if hasattr(self.approval_status, 'to_alipay_dict'):
                params['approval_status'] = self.approval_status.to_alipay_dict()
            else:
                params['approval_status'] = self.approval_status
        if self.balance_amount:
            if hasattr(self.balance_amount, 'to_alipay_dict'):
                params['balance_amount'] = self.balance_amount.to_alipay_dict()
            else:
                params['balance_amount'] = self.balance_amount
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.draw_amount:
            if hasattr(self.draw_amount, 'to_alipay_dict'):
                params['draw_amount'] = self.draw_amount.to_alipay_dict()
            else:
                params['draw_amount'] = self.draw_amount
        if self.draw_interest:
            if hasattr(self.draw_interest, 'to_alipay_dict'):
                params['draw_interest'] = self.draw_interest.to_alipay_dict()
            else:
                params['draw_interest'] = self.draw_interest
        if self.draw_item:
            if hasattr(self.draw_item, 'to_alipay_dict'):
                params['draw_item'] = self.draw_item.to_alipay_dict()
            else:
                params['draw_item'] = self.draw_item
        if self.draw_item_detail_id:
            if hasattr(self.draw_item_detail_id, 'to_alipay_dict'):
                params['draw_item_detail_id'] = self.draw_item_detail_id.to_alipay_dict()
            else:
                params['draw_item_detail_id'] = self.draw_item_detail_id
        if self.is_coextract:
            if hasattr(self.is_coextract, 'to_alipay_dict'):
                params['is_coextract'] = self.is_coextract.to_alipay_dict()
            else:
                params['is_coextract'] = self.is_coextract
        if self.item_creation_time:
            if hasattr(self.item_creation_time, 'to_alipay_dict'):
                params['item_creation_time'] = self.item_creation_time.to_alipay_dict()
            else:
                params['item_creation_time'] = self.item_creation_time
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_state:
            if hasattr(self.item_state, 'to_alipay_dict'):
                params['item_state'] = self.item_state.to_alipay_dict()
            else:
                params['item_state'] = self.item_state
        if self.operating_deck:
            if hasattr(self.operating_deck, 'to_alipay_dict'):
                params['operating_deck'] = self.operating_deck.to_alipay_dict()
            else:
                params['operating_deck'] = self.operating_deck
        if self.operating_time:
            if hasattr(self.operating_time, 'to_alipay_dict'):
                params['operating_time'] = self.operating_time.to_alipay_dict()
            else:
                params['operating_time'] = self.operating_time
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.rent_monthly_balance:
            if hasattr(self.rent_monthly_balance, 'to_alipay_dict'):
                params['rent_monthly_balance'] = self.rent_monthly_balance.to_alipay_dict()
            else:
                params['rent_monthly_balance'] = self.rent_monthly_balance
        if self.rental_type:
            if hasattr(self.rental_type, 'to_alipay_dict'):
                params['rental_type'] = self.rental_type.to_alipay_dict()
            else:
                params['rental_type'] = self.rental_type
        if self.trans_provincial_label:
            if hasattr(self.trans_provincial_label, 'to_alipay_dict'):
                params['trans_provincial_label'] = self.trans_provincial_label.to_alipay_dict()
            else:
                params['trans_provincial_label'] = self.trans_provincial_label
        if self.user_record_no:
            if hasattr(self.user_record_no, 'to_alipay_dict'):
                params['user_record_no'] = self.user_record_no.to_alipay_dict()
            else:
                params['user_record_no'] = self.user_record_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayQueryUserSignInfoResponse()
        if 'applicant_id' in d:
            o.applicant_id = d['applicant_id']
        if 'approval_status' in d:
            o.approval_status = d['approval_status']
        if 'balance_amount' in d:
            o.balance_amount = d['balance_amount']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'draw_amount' in d:
            o.draw_amount = d['draw_amount']
        if 'draw_interest' in d:
            o.draw_interest = d['draw_interest']
        if 'draw_item' in d:
            o.draw_item = d['draw_item']
        if 'draw_item_detail_id' in d:
            o.draw_item_detail_id = d['draw_item_detail_id']
        if 'is_coextract' in d:
            o.is_coextract = d['is_coextract']
        if 'item_creation_time' in d:
            o.item_creation_time = d['item_creation_time']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_state' in d:
            o.item_state = d['item_state']
        if 'operating_deck' in d:
            o.operating_deck = d['operating_deck']
        if 'operating_time' in d:
            o.operating_time = d['operating_time']
        if 'operator' in d:
            o.operator = d['operator']
        if 'rent_monthly_balance' in d:
            o.rent_monthly_balance = d['rent_monthly_balance']
        if 'rental_type' in d:
            o.rental_type = d['rental_type']
        if 'trans_provincial_label' in d:
            o.trans_provincial_label = d['trans_provincial_label']
        if 'user_record_no' in d:
            o.user_record_no = d['user_record_no']
        return o


