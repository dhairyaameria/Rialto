import React from "react";

// components

import CreditCard from "components/Cards/CreditCard.js";

// layout for page

import Admin from "layouts/Admin.js";

export default function Settings() {
  return (
    <>
      <div className="flex flex-wrap">
        <div className="w-full px-4">
          <CreditCard />
        </div>
      </div>
    </>
  );
}

Settings.layout = Admin;
