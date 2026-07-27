import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import {Hello} from './App.jsx'
import {tableData, renderingConstant, reactRenderingConstant, renderingWithBinding} from './Constants.jsx'


createRoot(document.getElementById('root')).render(
  /* USING CONSTANT AS RENDER */
  // tableData

  <StrictMode>
    <h1>Main component</h1>
    <Hello />
  </StrictMode>
)

createRoot(document.getElementById('base')).render(
  /* USING HTML AS RENDER */
  // <h1>Base Header</h1>
  renderingWithBinding
)